# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class illustrated_message_props(ui5_tag_props):
    name: Literal[
        "AddColumn",
        "AddPeople",
        "AddDimensions",
        "BalloonSky",
        "BeforeSearch",
        "Connection",
        "EmptyCalendar",
        "EmptyList",
        "EmptyPlanningCalendar",
        "ErrorScreen",
        "FilterTable",
        "GroupTables",
        "NoActivities",
        "NoColumnSet",
        "NoData",
        "NoEntries",
        "NoFilterResults",
        "NoMail_v1",
        "NoMail",
        "NoNotifications",
        "NoSavedItems",
        "NoSavedItems_v1",
        "NoSearchResults",
        "NoTasks",
        "NoTasks_v1",
        "NoDimensionsSet",
        "PageNotFound",
        "ReloadScreen",
        "ResizeColumn",
        "SearchEarth",
        "SearchFolder",
        "SimpleBallon",
        "SimpleBell",
        "SimpleCalendar",
        "SimpleCheckMark",
        "SimpleConnection",
        "SimpleEmptyDock",
        "SimpleEmptyList",
        "SimpleError",
        "SimpleMagnifier",
        "SimpleMail",
        "SimpleNoSavedItems",
        "SimpleNotFoundMagnifier",
        "SimpleReload",
        "SimpleTask",
        "SleepingBell",
        "SortColumn",
        "SuccessBalloon",
        "SuccessCheckMark",
        "SuccessHighFive",
        "SuccessScreen",
        "Survey",
        "Tent",
        "UnableToLoad",
        "UnableToLoadImage",
        "UnableToUpload",
        "UnableToUploadToCloud",
        "UploadCollection",
        "TntChartArea",
        "TntChartArea2",
        "TntChartBar",
        "TntChartBPMNFlow",
        "TntChartBullet",
        "TntChartDoughnut",
        "TntChartFlow",
        "TntChartGantt",
        "TntChartOrg",
        "TntChartPie",
        "TntCodePlaceHolder",
        "TntCompany",
        "TntComponents",
        "TntExternalLink",
        "TntFaceID",
        "TntFingerprint",
        "TntLock",
        "TntMission",
        "TntNoApplications",
        "TntNoFlows",
        "TntNoUsers",
        "TntRadar",
        "TntSecrets",
        "TntServices",
        "TntSessionExpired",
        "TntSessionExpiring",
        "TntSuccess",
        "TntSuccessfulAuth",
        "TntSystems",
        "TntTeams",
        "TntTools",
        "TntUnableToLoad",
        "TntUnlock",
        "TntUnsuccessfulAuth",
        "TntUser2",
    ]
    accessible_name_ref: str
    size: Literal["Auto", "Base", "Spot", "Dialog", "Scene"]
    subtitle_text: str
    title_text: str


class illustrated_message(ui5_tag):
    """<ui5-illustrated-message> An IllustratedMessage is a recommended combination of
    a solution-oriented message, an engaging illustration, and conversational tone to
    better communicate an empty or a success state than just show a message alone."""

    def __init__(self, *args, **kwargs: Unpack[illustrated_message_props]) -> None:
        self.tagname = "ui5-illustrated-message"
        super().__init__("ui5-illustrated-message", *args, **kwargs)
