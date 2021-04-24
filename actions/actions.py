# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import webbrowser
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionTPO(Action):
    def name(self) -> Text:
        return "action_tpo"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        tpo_url = "http://tpo.geca.ac.in/Default.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(tpo_url)
        return []


class PlacementRecordOfThirdFourth(Action):
    def name(self) -> Text:
        return "place_rec_third"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        link_url = "http://tpo.geca.ac.in/PlacementRecords2013-14.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(link_url)
        return []


# placement record of 2014 and 2015
class PlacementRecordOfFourthFifth(Action):
    def name(self) -> Text:
        return "placement_record_fourthfifth"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        link_url = "http://tpo.geca.ac.in/PlacementRecords2014-15.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(link_url)
        return []


# placement record of 2015 and 2016
class PlacementRecordOfFifteen(Action):
    def name(self) -> Text:
        return "place_recordOf_fifteensixteen"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        link_url = "http://tpo.geca.ac.in/PlacementRecords2015-16.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(link_url)
        return []


# placement record of 2016 and 2017
class PlacementRecordOfSeventeen(Action):
    def name(self) -> Text:
        return "placement_recordOf_serVenteen"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        link_url = "http://tpo.geca.ac.in/PlacementRecords2016-17.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(link_url)
        return []


# placement record of 2017 and 2018
class PlacementRecordOfLast(Action):
    def name(self) -> Text:
        return "placeme_record_lastofYear"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        link_url = "http://tpo.geca.ac.in/PlacementRecords2017-18.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(link_url)
        return []