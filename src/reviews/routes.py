from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from src.db.models import User
from src.db.main import get_session
from src.auth.dependencies import get_current_user, RoleChecker
from .schemas import ReviewCreateModel
from .service import ReviewService
from sqlmodel.ext.asyncio.session import AsyncSession

review_service = ReviewService()
review_router = APIRouter()
admin_role_checker = Depends(RoleChecker(["admin"]))
user_role_checker = Depends(RoleChecker(["user","admin"]))

@review_router.get("/", dependencies=[admin_role_checker])
async def get_all_reviews(session: AsyncSession = Depends(get_session)):
    reviews = await review_service.get_all_reviews(session)

    return reviews

@review_router.get("/{review_uid}", dependencies=[user_role_checker])
async def get_review(review_uid: str, session: AsyncSession = Depends(get_session)):
    review = await review_service.get_review(review_uid, session)

    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Review Not found"
        )
    return review

@review_router.post('/book/{book_uid}', dependencies=[user_role_checker])
async def add_review_to_book(book_uid: str, review_data: ReviewCreateModel, current_user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):

    new_review = await review_service.add_review_to_book(
        user_email = current_user.email,
        review_data = review_data,
        book_uid = book_uid,
        session = session
    )

    return new_review

@review_router.delete("/{review_uid}", dependencies=[user_role_checker], status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(review_uid: str, current_user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    await review_service.delete_review_to_from_book(
        review_uid=review_uid, user_email = current_user.email, session = session
    )

    return None