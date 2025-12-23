import dlt

expectations = {
  "rule_1":"user_id IS NOT NULL"
}

@dlt.table 
@dlt.expect_all_or_drop(expectations)
def dimUserStg():
  df = spark.readStream.table("spotify_catalog.silver.dimUser")
  return df

dlt.create_streaming_table("dimUser")

dlt.create_auto_cdc_flow(
 target= "dimUser",
 source="dimUserStg",
 keys = ["user_id"],
 sequence_by="updated_at",
 stored_as_scd_type=2,
 track_history_except_column_list = None,
 name=None,
 once=False
)