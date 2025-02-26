from dataclasses import dataclass, field

from environs import Env


@dataclass
class RunConfig:
    api_host: str
    api_port: int

    @staticmethod
    def from_env(env: str) -> "RunConfig":
        return RunConfig(
            api_host=env.str("API_HOST"),
            api_port=env.int("API_PORT"),
        )


@dataclass
class AccessTokenConfig:
    token_secret: str
    algorithm: str = "HS256"
    token_expire_seconds: int = 3600

    @staticmethod
    def from_env(env: Env) -> "AccessTokenConfig":
        return AccessTokenConfig(
            token_secret=env.str("TOKEN_SECRET"),
        )


@dataclass
class ApiV1Prefix:
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    tasks: str = "/tasks"


@dataclass
class ApiPrefix:
    prefix: str = "/api"
    v1: ApiV1Prefix = field(default=ApiV1Prefix)

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")
