# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import webbrowser
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from db_con import *
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


# Email Action
class ActionDemoEmail(Action):
    def name(self):
        return 'send_email_sender'

    def run(self, dispatcher, tracker, domain):
        import os
        import smtplib
        from email.message import EmailMessage

        msg = EmailMessage()
        msg['Subject'] = 'GECA Support'
        msg['From'] = 'mainon.geca@gmail.com'  # sender's email address
        msg['To'] = tracker.get_slot("sender_email")  # receiver's email address

        msg.set_content(
            'Hello Dear {},\n \n      Thank you for your response, your query on {} is successfully submitted.  As '
            'soon as possible we will get in touch with you! \n \n \n \n \n Thank You '.format(
                tracker.get_slot("sender_name"), tracker.get_slot("sender_message"))
        )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('mainon.geca@gmail.com', 'Pass-Pass#7890')
            smtp.send_message(msg)
        dispatcher.utter_message("Your Email has send")

    # remaining Content

    class ActionAdmission(Action):
        def name(self) -> Text:
            return "action_admission"

        async def run(
                self,
                dispatcher,
                tracker: Tracker,
                domain: "DomainDict",
        ) -> List[Dict[Text, Any]]:
            dispatcher.utter_message("wait... you are redirected")
            url = "http://www.dtemaharashtra.gov.in/index.html"
            webbrowser.open(url)
            return []

    class ActionStudentSection(Action):
        def name(self) -> Text:
            return "action_studentsection"

        async def run(
                self,
                dispatcher,
                tracker: Tracker,
                domain: "DomainDict",
        ) -> List[Dict[Text, Any]]:
            dispatcher.utter_message("wait... you are redirected")
            url = "http://geca.ac.in/home.aspx"
            webbrowser.open(url)
            return []

        class ActionScholarship(Action):
            def name(self) -> Text:
                return "action_scholarship"

            async def run(
                    self,
                    dispatcher,
                    tracker: Tracker,
                    domain: "DomainDict",
            ) -> List[Dict[Text, Any]]:
                url = "https://mahadbtmahait.gov.in"
                dispatcher.utter_message("wait... you are redirected")
                webbrowser.open(url)
                return []

        class ActionEducationLoan(Action):
            def name(self) -> Text:
                return "action_educationloan"

            async def run(
                    self,
                    dispatcher,
                    tracker: Tracker,
                    domain: "DomainDict",
            ) -> List[Dict[Text, Any]]:
                dispatcher.utter_message("wait... you are redirected")
                url = "https://www.vidyalakshmi.co.in/Students"
                webbrowser.open(url)
                return []

            class ActionMISLogin(Action):
                def name(self) -> Text:
                    return "action_mis_login"

                async def run(
                        self,
                        dispatcher,
                        tracker: Tracker,
                        domain: "DomainDict",
                ) -> List[Dict[Text, Any]]:
                    dispatcher.utter_message("You are log in :)")
                    return []

                class ActionStudentDetailsLogin(Action):
                    def name(self) -> Text:
                        return "action_student_details"

                    async def run(
                            self,
                            dispatcher,
                            tracker: Tracker,
                            domain: "DomainDict",
                    ) -> List[Dict[Text, Any]]:
                        dispatcher.utter_message("Your Student Details here ! ")
                        return []

                    class ActionCourseRegistrationLogin(Action):
                        def name(self) -> Text:
                            return "action_course_registration"

                        async def run(
                                self,
                                dispatcher,
                                tracker: Tracker,
                                domain: "DomainDict",
                        ) -> List[Dict[Text, Any]]:
                            dispatcher.utter_message("Your Course Registration has done ")
                            return []


# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_details_thanks",
#                                  UserName=tracker.get_slot("uname"),
#                                  Password=tracker.get_slot("passwd"))
#         insert_data(tracker.get_slot("uname"), tracker.get_slot("passwd"))
#         dispatcher.utter_message("Thanks for valuable feedback")
#
#         return []
#
# class ActionFetch(Action):
#     f1=0
#     def name(self) -> Text:
#         return "action_Fetch"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_message")
#         r = fetch_data()
#         for i in r:
#
#
#             if (tracker.get_slot("uname")==i[0] and tracker.get_slot("passwd")==i[1]):
#                 dispatcher.utter_message(template="utter_greetagain")
#                 ActionFetch.f1=1
#                 dispatcher.utter_message(template="utter_academicchoices")
#                 break
#         else:
#             dispatcher.utter_message(text="Username password mismatch !\n")
#             dispatcher.utter_message(response="utter_next")
#             return [SlotSet("uname", None),SlotSet("passwd", None)]
#         return[]
#
#
#
#
#
#
# class ActionStudentDetails(Action):
#     f=0
#     def name(self) -> Text:
#         return "action_StudentDetails"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         if (tracker.get_slot("uname")!=None and tracker.get_slot("passwd")!=None):
#
#             result=fetch_details(tracker.get_slot("uname"))
#             for i in result:
#                 f=1
#                 dispatcher.utter_message(text="name:",end="")
#                 dispatcher.utter_message(i[0])
#                 dispatcher.utter_message(text="father name:")
#                 dispatcher.utter_message(i[1])
#                 dispatcher.utter_message("rollno:")
#                 dispatcher.utter_message(i[2])
#                 dispatcher.utter_message("faculty advisor:")
#                 dispatcher.utter_message(i[3])
#                 dispatcher.utter_message("mobile no:")
#                 dispatcher.utter_message(str(i[4]))
#                 dispatcher.utter_message("religion:")
#                 dispatcher.utter_message(i[5])
#                 dispatcher.utter_message("semester")
#                 dispatcher.utter_message(str(i[6]))
#
#         if f==0:
#             dispatcher.utter_message(text="You haven't logged in for this activity. Please log in .")
#
#
#
#         return []
#
# class  ActionNullify(Action):
#     def name(self) -> Text:
#         return "action_Nullify"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="OK initiating for another user login")
#
#         return [SlotSet("uname", None),SlotSet("passwd", None)]
#
#
#
# class ActionCourseRegistration(Action):
#     def name(self) -> Text:
#         return "action_CourseRegistration"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         d={
#             1:["Basics of Computer Science","Physics","Chemistry","Engg. Mathematics"],
#             2:["Engg.Mathematics","C programming","Physics","Chemistry"],
#             3:["Engg.Mathematics","Database Management Systems","Core Java","Psychology","EVS","EDP"],
#             4:["Data Structures","Computwer Organization","PECS","OSST","Lab-DS","Lab-Advance Java"],
#             5:["TOC","OS","DAA","TQM","Software Engineering","Mini project"],
#             6:["Computer Networks","Data Science","NNDL","Advanced Algorithm","Distributed Databases"],
#             7:["NLP","Cloud Computing","Big Dta","Project-1"],
#             8:["Project-2"]
#         }
#
#         if (tracker.get_slot("uname")!=None and tracker.get_slot("passwd")!=None):
#             cur_sem=get_sem(tracker.get_slot("uname"))
#             for i in d[cur_sem[0]]:
#                 dispatcher.utter_message(i)
#
#         else:
#             dispatcher.utter_message(text="You haven't logged in for this activity. Please log in .")
#
#
#         return []
#
#
#
# class ActionOptionalCourse(Action):
#     def name(self) -> Text:
#         return "action_OptionalCourse"
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         addoptcourse(tracker.get_slot("uname"),tracker.get_slot("optsub"))
#         dispatcher.utter_message(text="Course added Successfully !")
#
#         return [SlotSet("optsub", None)]