from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
    columns={
        "OrderID": Column(dtype="string[python]"),
        "Date": Column(dtype="string[python]"),
        "CustomerID": Column(dtype="string[python]"),
        "Quantity": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=5.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "UnitPrice": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=11.39, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=699.93, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "ShippingAddress": Column(dtype="string[python]"),
        "TrackingNumber": Column(dtype="string[python]"),
        "ItemsInCart": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=10.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "TotalPrice": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=11.39, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=3330.4075, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Desk": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Laptop": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Monitor": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Phone": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Printer": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "Product_Tablet": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "PaymentMethod_Credit Card": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "PaymentMethod_Debit Card": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "PaymentMethod_Gift Card": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "PaymentMethod_Online": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "OrderStatus_Delivered": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "OrderStatus_Pending": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "OrderStatus_Returned": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "OrderStatus_Shipped": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "CouponCode_SAVE10": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "CouponCode_WINTER15": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "ReferralSource_Facebook": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "ReferralSource_Google": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "ReferralSource_Instagram": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
        "ReferralSource_Referral": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
        ),
    },
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(
                min_value=0.0, raise_warning=False, ignore_na=True
            ),
            Check.less_than_or_equal_to(
                max_value=1199.0, raise_warning=False, ignore_na=True
            ),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    coerce=True,
)
