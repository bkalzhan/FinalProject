USER_ROLE_SUPER_USER = 1
USER_ROLE_STAFF = 2
USER_ROLE_CUSTOMER = 3
USER_ROLES = (
    (USER_ROLE_SUPER_USER, 'super admin'),
    (USER_ROLE_STAFF, 'staff'),
    (USER_ROLE_CUSTOMER, 'customer'),
)

rating_numbers = (
        (1, "One-Star"),
        (2, "Two-Star"),
        (3, "Three-Star"),
        (4, "Four-Star"),
        (5, "Five-Star")
    )
subscription_type = (
    ("MORNING", "Morning Subscription"),
    ("DAY", "Day Subscription"),
    ("EVENING", "Evening Subscription"),
    ("UNLIMITED", "Unlimited Subscription")
)
status_choices = (
        (1, "Paid"),
        (0, "Unpaid"),
    )
