# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict

import pandas as pd
from statsmodels.tsa.statespace.tools import diff

def split_data(data: pd.DataFrame, example_test_data_ratio: float) -> Dict[str, Any]:
    """Node for splitting the data set into training and test
    sets.
    The split ratio parameter is taken from conf/project/parameters.yml.
    The data and the parameters will be loaded and provided to your function
    automatically when the pipeline is executed and it is time to run this node.
    """

    if data.empty or len(data) < 30:
        print('Data provided are too short!')
        # return dict(
        #             train_y=[],
        #             test_y=[],
        #             n=0,
        #         )
        raise ValueError('Data provided are too short!')


    uem = pd.Series(data=list(data['unempl_m']),
    index=pd.date_range('1994-01-01', periods=len(data), freq='M')).dropna()

    uemd = diff(uem)

    uemd_train = uemd.iloc[:round(len(uemd)*(1-example_test_data_ratio))]
    uemd_test = uemd.iloc[round(len(uemd)*example_test_data_ratio):]

    # When returning many variables, it is a good practice to give them names:
    return dict(
        #train_x=train_data_x,
        train_y=uemd_train,
        #test_x=test_data_x,
        test_y=uemd_test,
        n=len(uemd),
        )
