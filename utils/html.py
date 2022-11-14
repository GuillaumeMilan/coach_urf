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

    def lane_index(self, lane):
        if lane == "SOLO TOP":
            return 0
        if lane == "NONE JUNGLE":
            return 1
        if lane == "SOLO MIDDLE":
            return 2
        if lane == "DUO_CARRY BOTTOM":
            return 3
        if lane == "DUO_SUPPORT BOTTOM":
            return 4
        print("[ERROR] Unrecognized position", lane)
        return 100
    def sorted_champions(self):
        champion = [champion for i, champion in self.summary.items()]
        champion.sort(key=lambda c: self.lane_index(c['lane']))
        return champion
    def repr_head(self):
        return f"""<thead><tr>
                <th>Game ID</th>
                <th>Name</th>
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
                <th>Lane</th>
            </tr></thead>"""
    def repr_row(self, champion):
        return f"""<tr>
                <td>{champion['id']}</td>
                <td>{champion['name']}</td>
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
                <td>{champion['lane']}</td>
            </tr>"""
    def repr_body(self):
        return f"""<tbody>{''.join([self.repr_row(champion) for champion in self.sorted_champions()])}</tbody>"""
    def _repr_html_(self):
        return f"""<table>{self.repr_head()}{self.repr_body()}</table>"""
