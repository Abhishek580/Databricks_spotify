import dlt

@dlt.table
def factStreamStg():
  df = spark.readStream.table("spotify_catalog.silver.factstream")
  return df

dlt.create_streaming_table("factstream")

dlt.create_auto_cdc_flow(
 target= "factstream",
 source="factStreamStg",
 keys = ["stream_id"],
 sequence_by="stream_timestamp",
 stored_as_scd_type=2,
 track_history_except_column_list = None,
 name=None,
 once=False
)