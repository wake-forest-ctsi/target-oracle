"""Oracle target sink class, which handles writing streams."""

from typing import Any, Dict, Iterable, Optional

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

    def bulk_insert_records(
        self,
        full_table_name: str,
        schema: dict,
        records: Iterable[Dict[str, Any]],
    ) -> Optional[int]:
        """Bulk insert records to an existing destination table.

        The default implementation uses a generic SQLAlchemy bulk insert operation.
        This method may optionally be overridden by developers in order to provide
        faster, native bulk uploads.

        Args:
            full_table_name: the target table name.
            schema: the JSON schema for the new table, to be used when inferring column
                names.
            records: the input records.

        Returns:
            True if table exists, False if not, None if unsure or undetectable.
        """
        table = self.connector.get_table(full_table_name)

        self.connection.execute(
            table.insert(),
            records,
        )

        if isinstance(records, list):
            return len(records)  # If list, we can quickly return record count.

        return None  # Unknown record count.