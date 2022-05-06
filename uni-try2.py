# %%
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from datetime import datetime
from subgrounds.subgraph import SyntheticField
import plotly.express as px


# %%
from subgrounds.subgrounds import Subgrounds

sg = Subgrounds()
uniarb = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-minimal')
uniop =  sg.load_subgraph('https://api.thegraph.com/subgraphs/name/ianlapham/optimism-post-regenesis')
unipol = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-polygon')

crvop = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/convex-community/volume-optimism')
crvarb = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/convex-community/volume-arbitrum')
crvpol = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/convex-community/volume-matic')


# %%
"""
#uniswap-arbitrum volume
"""

# %%
voluniarb = uniarb.Query.uniswapDayDatas(
    first = 1000,
    orderby = uniarb.UniswapDayData.date,
    orderDirection = 'desc'
)


uniarb.UniswapDayData.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    uniarb.UniswapDayData.date
)

# %%
duniarb = sg.query_df([voluniarb.volumeUSD,voluniarb.datetime])

# %%
#duniarb

# %%
figuniarb = px.bar(duniarb, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 


# %%
"""
uniswap-optimism
"""

# %%
voluniop = uniop.Query.uniswapDayDatas(
    first = 1000,
    orderby = uniop.UniswapDayData.date,
    orderDirection = 'desc'
)


uniop.UniswapDayData.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    uniop.UniswapDayData.date
)

duniop = sg.query_df([voluniop.volumeUSD,voluniop.datetime])

figuniop = px.bar(duniop, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 


# %%
"""
#uniswap-polygon
"""

# %%
volunipol = unipol.Query.uniswapDayDatas(
    first = 1000,
    orderby = unipol.UniswapDayData.date,
    orderDirection = 'desc'
)


unipol.UniswapDayData.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    unipol.UniswapDayData.date
)

dunipol = sg.query_df([volunipol.volumeUSD,volunipol.datetime])

figunipol = px.bar(duniop, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 


# %%
"""
#curve-arb
"""

# %%
volcrvarb = crvarb.Query.dailySwapVolumeSnapshots(
    first = 2000,
    orderBy = crvarb.DailySwapVolumeSnapshot.timestamp,
    orderDirection = 'desc'
)

crvarb.DailySwapVolumeSnapshot.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    crvarb.DailySwapVolumeSnapshot.timestamp
)

dcrvarb = sg.query_df([volcrvarb.volumeUSD,volcrvarb.datetime,volcrvarb.pool.name])

# %%
figcrvarb = px.bar(dcrvarb, x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD") 

figcrvarb.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)


# %%
"""
curve-optimism
"""

# %%
volcrvop = crvop.Query.dailySwapVolumeSnapshots(
    first = 2000,
    orderBy = crvop.DailySwapVolumeSnapshot.timestamp,
    orderDirection = 'desc'
)

crvop.DailySwapVolumeSnapshot.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    crvop.DailySwapVolumeSnapshot.timestamp
)

dcrvop = sg.query_df([volcrvop.volumeUSD,volcrvop.datetime])

figcrvop = px.bar(dcrvop, x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD") 

figcrvop.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)



# %%
"""
#curve-polygon
"""

# %%
volcrvpol = crvpol.Query.dailySwapVolumeSnapshots(
    first = 20000,
    orderBy = crvpol.DailySwapVolumeSnapshot.timestamp,
    orderDirection = 'desc'
)

crvpol.DailySwapVolumeSnapshot.datetime = SyntheticField(
    lambda date: str(datetime.fromtimestamp(date).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    crvpol.DailySwapVolumeSnapshot.timestamp
)

dcrvpol = sg.query_df([volcrvpol.volumeUSD,volcrvpol.datetime])

figcrvop = px.bar(dcrvop, x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD") 

figcrvop.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)

# %%
"""
#streamlit work
"""

# %%
st.title("Uniswap daily swapping volume on different L2s")

# %%
