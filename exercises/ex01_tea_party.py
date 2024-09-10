"""Tea Party!"""

__author__ = "730751173"
"""Plan a cozy tea party"""


def main_planner(guests: int) -> None:
    """Print the output of all functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """everyone will have two tea bags"""
    return people * 2


def treats(people: int) -> int:
    """For each tea, they will have 1.5 snacks"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
