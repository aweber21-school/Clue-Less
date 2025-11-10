"""Constants for the Clue-Less Application"""

CHARACTER_COLORS = {
    "MissScarlett": (255, 0, 0),
    "ColonelMustard": (255, 255, 0),
    "MrsWhite": (235, 235, 235),
    "MrGreen": (0, 255, 0),
    "MrsPeacock": (0, 0, 255),
    "ProfessorPlum": (128, 0, 128),
}

LOCATION_NAMES = [
    ["Study", "StudyHall", "Hall", "HallLounge", "Lounge"],
    ["StudyLibrary", None, "HallBilliard", None, "LoungeDining"],
    ["Library", "LibraryBilliard", "Billiard", "BilliardDining", "Dining"],
    ["LibraryConservatory", None, "BilliardBallroom", None, "DiningKitchen"],
    [
        "Conservatory",
        "ConservatoryBallroom",
        "Ballroom",
        "BallroomKitchen",
        "Kitchen",
    ],
]

"""Origin is Study (0,0) (-y,x)"""
STARTING_LOCATIONS = {
    "MissScarlett": (0, 3),
    "ColonelMustard": (1, 4),
    "MrsWhite": (4, 3),
    "MrGreen": (4, 1),
    "MrsPeacock": (3, 0),
    "ProfessorPlum": (1, 0),
}
