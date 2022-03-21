"""Oracle target sink class, which handles writing streams."""

from singer_sdk.sinks import SQLSink
import sqlalchemy

from target_oracle.connector import OracleConnector


class OracleSink(SQLSink):
    """The Sink class for Oracle.

    This class allows developers to optionally override `get_records()` and other
    stream methods in order to improve performance beyond the default SQLAlchemy-based
    interface.

    DDL and type conversion operations are delegated to the connector logic specified
    in `connector_class` or by overriding the `connector` object.
    """

    soft_delete_column_name = "sdc_deleted_at"
    version_column_name = "sdc_table_version"

    connector_class = OracleConnector

    def activate_version(self, new_version: int) -> None:
        """Bump the active version of the target table.

        Args:
            new_version: The version number to activate.
        """

        # temporary fix, parents don't seem to handle activate messages where table does not exist
        if self.connector.table_exists(full_table_name=self.full_table_name):
            super().activate_version(new_version)