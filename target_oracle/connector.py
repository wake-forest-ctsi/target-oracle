from typing import Any, Dict

import sqlalchemy
from singer_sdk import SQLConnector


class OracleConnector(SQLConnector):
    """The connector for Oracle.

    This class handles all DDL and type conversions.
    """

    allow_temp_tables = False
    allow_column_alter = False
    allow_merge_upsert = True

    def get_sqlalchemy_url(self, config: Dict[str, Any]) -> str:
        """Generates a SQLAlchemy URL for Oracle."""
        url = sqlalchemy.engine.url.URL.create(**{k:v for k, v in config.items() if k in ('drivername','username','password','host','port','database','query')})
        return str(url)

    def create_sqlalchemy_connection(self) -> sqlalchemy.engine.Connection:
        """Return a new SQLAlchemy connection using the provided config.

        This override simply provides a more helpful error message on failure.

        Returns:
            A newly created SQLAlchemy engine object.
        """
        try:
            return super().create_sqlalchemy_connection()
        except Exception as ex:
            raise RuntimeError(
                f"Error connecting to DB at '{self.config['drivername']}://{self.config['username']}:<redacted>@{self.config['host']}:{self.config['port']}/{self.config['database']}"
            ) from ex

    @staticmethod
    def to_sql_type(jsonschema_type: dict) -> sqlalchemy.types.TypeEngine:
        """Return a JSON Schema representation of the provided type.

        By default will call `typing.to_sql_type()`.

        Developers may override this method to accept additional input argument types,
        to support non-standard types, or to provide custom typing logic.

        If overriding this method, developers should call the default implementation
        from the base class for all unhandled cases.

        Args:
            jsonschema_type: The JSON Schema representation of the source type.

        Returns:
            The SQLAlchemy type representation of the data type.
        """

        sqltype = super().to_sql_type(jsonschema_type)
        
        if type(sqltype) == sqlalchemy.types.VARCHAR:
            sqltype = sqlalchemy.types.VARCHAR(255)

        return sqltype