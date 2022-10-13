from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "password" VARCHAR(256) NOT NULL,
    "last_login" TIMESTAMP NOT NULL,
    "is_superuser" INT NOT NULL,
    "username" VARCHAR(512) NOT NULL,
    "first_name" VARCHAR(512) NOT NULL,
    "last_name" VARCHAR(512) NOT NULL,
    "email" VARCHAR(512) NOT NULL,
    "is_staff" INT NOT NULL  DEFAULT 0,
    "is_active" INT NOT NULL  DEFAULT 1,
    "username_discriminator" INT NOT NULL,
    "avatar" VARCHAR(512) NOT NULL,
    "avatar_provider" VARCHAR(512) NOT NULL,
    "ip" VARCHAR(512) NOT NULL,
    "date_joined" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
