import utils.html
import utils.dragon

class MatchSummary:
    def __init__(self, match, session):
        self._match = match
        self._session = session

    def scoreTable(self):
        return {participant['participantId'] : {'champion': self._session.image_from_champion(f"{participant['championId']}"),
        'items': [
            self._session.image_from_item(participant['stats']['item0']),
            self._session.image_from_item(participant['stats']['item1']),
            self._session.image_from_item(participant['stats']['item2']),
            self._session.image_from_item(participant['stats']['item3']),
            self._session.image_from_item(participant['stats']['item4']),
            self._session.image_from_item(participant['stats']['item5']),
            self._session.image_from_item(participant['stats']['item6'])
            ],
        'kills' : participant['stats']['kills'],
        'assists': participant['stats']['assists'],
        'deaths': participant['stats']['deaths'],
        'totalMinionsKilled': participant['stats']['totalMinionsKilled'],
        'goldEarned': participant['stats']['goldEarned'],
        'win': participant['stats']['win']
        } for participant in self._match['participants']}


    def _repr_html_(self):
        return f"""
        <h1>WIN</h1>
        {utils.html.SummaryTable({id : value for id, value in self.scoreTable().items() if value['win']})._repr_html_()}
        <h1>DEFEAT</h1>
        {utils.html.SummaryTable({id : value for id, value in self.scoreTable().items() if not value['win']})._repr_html_()}
        """
