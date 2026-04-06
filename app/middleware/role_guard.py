from fastapi import HTTPException, Depends
from typing import List

from ..api.deps import get_current_user


def require_role(allowed_roles: List[str]):
    """
    Dependency that restricts endpoint access based on user roles
    """

    def role_checker(user=Depends(get_current_user)):

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Authentication required"
            )

        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="You do not have permission to perform this action"
            )

        return user

    return role_checker