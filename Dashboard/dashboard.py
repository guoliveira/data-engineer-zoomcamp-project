import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash()

df = pd.read_parquet(
    "/mnt/c/Users/LuisSousaOliveira/Documents/Pessoal/Formação/Capstone/data/part-00000-3e7efa9c-0437-4776-af30-23a519131488-c000.snappy.parquet"
)


df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df= df.sort_values(by='date', ascending=False)

fig = px.line(
    df,
    x="date",
    y="TAVG",
    color="stations_code",
)

app.layout = html.Div([dcc.Graph(id="Avg-temp-over-one-year", figure=fig)])

# http://127.0.0.1:8050/

if __name__ == "__main__":
    app.run_server(debug=True)