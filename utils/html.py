import utils.dict_utils

class BinaryImage:
    def __init__(self, base64):
        self.base64 = base64

    def _repr_html_(self):
        return f"""<img src="data:image/png;base64, {self.base64}"/>"""

class Image:
    def __init__(self, src, height = '50px', width = '50px'):
        self.src = src
        self.width = width
        self.height = height
    def _repr_html_(self):
        return f"""<img src="{self.src}" height="{self.height}" width="{self.width}"/>"""

class SummaryTable:
    def __init__(self, summary):
        self.summary = summary

    def repr_head(self):
        return f"""<thead><tr>
                <th>Champion</th>
                <th></th>
                <th></th>
                <th></th>
                <th></th>
                <th></th>
                <th></th>
                <th></th>
                <th>K</th>
                <th>D</th>
                <th>A</th>
                <th>Gold</th>
                <th>Minions</th>
            </tr></thead>"""
    def repr_row(self, champion):
        return f"""<tr>
                <td>{champion['champion']}</td>
                <td>{champion['items'][0]}</td>
                <td>{champion['items'][1]}</td>
                <td>{champion['items'][2]}</td>
                <td>{champion['items'][3]}</td>
                <td>{champion['items'][4]}</td>
                <td>{champion['items'][5]}</td>
                <td>{champion['items'][6]}</td>
                <td>{champion['kills']}</td>
                <td>{champion['deaths']}</td>
                <td>{champion['assists']}</td>
                <td>{champion['goldEarned']}</td>
                <td>{champion['totalMinionsKilled']}</td>
            </tr>"""
    def repr_body(self):
        return f"""<tbody>{''.join([self.repr_row(champion) for id, champion in self.summary.items()])}</tbody>"""
    def _repr_html_(self):
        return f"""<table>{self.repr_head()}{self.repr_body()}</table>"""
