import utils.html
import utils.dragon

class MatchSummary:
    def __init__(self, match, session, timeline = None):
        self._match = match
        self._timeline = timeline
        self._session = session

    def identities_dict(self):
        return {participant['participantId'] : participant['player'] for participant in self._match['participantIdentities']}

    #def AnalyseJunglePath(self):
    #    if not self._timeline:
    #        return {}
    #    # TODO Analyse jugnle
    #    # 100 is blue side
    #    # 200 is red side
    #    return {
    #            '100'{
    #                }
    #            '200': {
    #                }
    #            }
    def isWinner(self, accountId = None, summonerName = None, summonerId = None, participantId = None):
        participantId = participantId
        if accountId:
            participantId = [p for p in self._match['participantIdentities'] if p['player']['accountId'] == accountId][0]['participantId']
        if summonerName:
            participantId = [p for p in self._match['participantIdentities'] if p['player']['summonerName'] == summonerName][0]['participantId']
        if summonerId:
            participantId = [p for p in self._match['participantIdentities'] if p['player']['summonerId'] == summonerId][0]['participantId']
        participant = [p for p in self._match['participants'] if p['participantId'] == participantId][0]
        team = [t for t in self._match['teams'] if t['teamId'] == participant['teamId']][0]
        if team['win'] == 'Win':
            return True
        return False


    def scoreTable(self):
        identities = self.identities_dict()
        return {participant['participantId'] : {
        'id': participant['participantId'],
        'name': identities[participant['participantId']]['summonerName'],
        'champion': self._session.image_from_champion(f"{participant['championId']}"),
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
        'lane': f"{participant['timeline']['role']} {participant['timeline']['lane']}",
        'win': participant['stats']['win']
        } for participant in self._match['participants']}

    def winners(self):
        return [i for i, v in self.scoreTable().items() if v['win']]

    def _repr_html_(self):
        return f"""
        <h1>WIN</h1>
        {utils.html.SummaryTable({id : value for id, value in self.scoreTable().items() if value['win']})._repr_html_()}
        <h1>DEFEAT</h1>
        {utils.html.SummaryTable({id : value for id, value in self.scoreTable().items() if not value['win']})._repr_html_()}
        """
