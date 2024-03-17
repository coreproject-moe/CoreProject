from gqlauth.user.queries import UserQueries
from gqlauth.user import relay as mutations
import strawberry


@strawberry.type
class Query(UserQueries):
    # you can add your queries here
    ...


@strawberry.type
class Mutation:
    # include what-ever mutations you want.
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    # swap_emails = mutations.SwapEmails.field
    # verify_secondary_email = mutations.VerifySecondaryEmail.field
    # captcha = Captcha.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field


schema = strawberry.Schema(query=Query, mutation=Mutation)
