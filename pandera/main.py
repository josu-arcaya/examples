import pandas as pd
import pandera.pandas as pa

def validate_model(df: pd.DataFrame) -> pd.DataFrame:

    class Schema(pa.DataFrameModel):
        column1: int = pa.Field(ge=0)
        column2: float = pa.Field(lt=10)
        column3: str = pa.Field(isin=[*"abc"])

        @pa.check("column3")
        def custom_check(cls, series: pd.Series) -> pd.Series:
            return series.str.len() == 1

    return Schema.validate(df)

def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    schema = pa.DataFrameSchema({
        "column1": pa.Column(int, [pa.Check.ge(0), pa.Check.le(3)]),
        "column2": pa.Column(float, pa.Check.lt(10)),
        "column3": pa.Column(
            str,
            [
                pa.Check.isin([*"abc"]),
                pa.Check(lambda series: series.str.len() == 1),
            ]
        ),
    }
    )
    return schema.validate(df)

def main():
    # data to validate
    df = pd.DataFrame({
        "column1": [1, 2, 3],
        "column2": [1.1, 1.2, 1.3],
        "column3": ["a", "b", "c"],
    })

    validated_df = validate_model(df)
    print(validated_df)

    validated_df = validate_schema(df)
    print(validated_df)


if __name__ == "__main__":
    main()
