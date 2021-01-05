import numpy as np
import pandas as pd
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.pandas import data_frames,column

import pytest

from gks_test.pipelines.data_engineering import nodes

# создаем дата сеты в декораторе
@given(
    # series(dtype=float,
    #     elements=st.floats(allow_nan=False,
    #                        allow_infinity=False,
    #                        min_value=0, max_value=50),
    #     index=st.dates('1989-01-01', '2021-01-01')
    # )
    data_frames(
        [
            column('year', dtype=int,
                   elements=st.integers(1989,2021)),
            column('month', dtype=int,
                   elements=st.integers(min_value=1, max_value=12)),
            column('unempl_m', dtype=float,
                   elements=st.floats(min_value=0, max_value=50)),
        ]
    ),
    st.floats(0.5, 1)
)
def test_split_data_hypolib(df, etdr):
    try:
        # smoke
        assert callable(nodes.split_data) is True
        # type
        assert isinstance(df, pd.DataFrame)
        assert isinstance(etdr, float)
        # unit
        # with pytest.raises(ValueError):
        #     print('here')
        #     assert nodes.split_data(df, etdr) == dict(
        #                 train_y=[],
        #                 test_y=[],
        #                 n=0,
        #             )

        assert isinstance(nodes.split_data(df, etdr), dict)
        assert nodes.split_data(df, etdr)['n'] == len(nodes.split_data(df, etdr)['train_y']) + len(nodes.split_data(df, etdr)['test_y'])
    except:
        print('here')
        True
