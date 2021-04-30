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

class ActionCivil(Action):
    def name(self) -> Text:
        return "action_Civil_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        civil_url = "http://geca.ac.in/dep-civil-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(civil_url)
        return []


class ActionElectrical(Action):
    def name(self) -> Text:
        return "action_ele_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        ele_url = "http://geca.ac.in/dep-elect-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(ele_url)
        return []


class ActionMech(Action):
    def name(self) -> Text:
        return "action_Mech_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        mech_url = "http://geca.ac.in/dep-mech-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(mech_url)
        return []


class ActionCSE(Action):
    def name(self) -> Text:
        return "action_CSE_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        cse_url = "http://geca.ac.in/dep-cse-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(cse_url)
        return []


class ActionET(Action):
    def name(self) -> Text:
        return "action_ET_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        ET_url = "http://geca.ac.in/dep-entc-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(ET_url)
        return []



class ActionITechology(Action):
    def name(self) -> Text:
        return "action_IT_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        I_url = "http://geca.ac.in/dep-it-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(I_url)
        return []


class ActionMCA(Action):
    def name(self) -> Text:
        return "action_MCA_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        mca_url = "http://geca.ac.in/dep-mca-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(mca_url)
        return []


class ActionScience(Action):
    def name(self) -> Text:
        return "action_Science_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        science_url = "http://geca.ac.in/dep-asci-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(science_url)
        return []


class ActionMath(Action):
    def name(self) -> Text:
        return "action_Math_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        math_url = "http://geca.ac.in/dep-math-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(math_url)
        return []


class ActionMechanics(Action):
    def name(self) -> Text:
        return "action_Mechanics_Details"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        mechanics_url = "http://geca.ac.in/dep-amech-home.aspx"
        dispatcher.utter_message("wait... you are redirected")
        webbrowser.open(mechanics_url)
        return []
