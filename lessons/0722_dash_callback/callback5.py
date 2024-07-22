from dash import Dash, html, dcc, Input, Output, callback, dash_table
import data
import pandas as pd

app = Dash(__name__)

areas = [tup[0] for tup in data.get_areas()]
app.layout = html.Div([
    dcc.Dropdown(
        options = areas,
        value = areas[0],
        id='areas'
    ),
    html.Hr(),

    dash_table.DataTable(id='sites_table')
])

@callback(
    Output('sites_table','data'),
    Input('areas','value')
)

def selected_area(areas_value):
    content = data.get_snaOfArea(area=areas_value)
    df = pd.DataFrame(content)
    df.columns = ['Site', 'Total', 'Bikes', 'Spots', 'Date', 'Status']
    return df.to_dict('records')

if __name__ == '__main__':
    app.run(debug=True)