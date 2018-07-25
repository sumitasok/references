[Index](index.md)

---

Architecture - Templating and Sending Emails using third party

I will try keep this language agnostic. This architecture talks about defining a system, which can once set, reduce the engineer interaction for any further template additions. This will handle certain real life scenarios which pulls engineers into template changes, and how to avoid those.

Scenario:

There is an email sender provider(internal or external) which can take variables as key-value pair and send the emails. Our system calls those services for a plathora of requests. Be it _transactional_, be it _marketting_. Be it _reminders_ or _status updates_.

- When an Order is placed for movie ticketing, the buyer is send with an email, that will have the order payment details, voucher details, event details, and terms and codition. (member)
- Reminder for the show with the above details except terms and conditions.
- Show recommendations, based on past history for upsell. (collection)
- Every event organiser is send with an update of how many purchased where done and how many cancellations where done today. (collection)
- Before event, organisers are send the final list. (collection)

Identifying the key players in the system.

- resource (Order, Organiser, User)
- receiver (Organiser, User)
- type of communication (Acknowledgement, Reminder, Status Update.
- individual template (under each type of communication, multple templates are used per receiver/resource/combination).



How to fetch a config?

- Is the value available in cache.
- Does this have a custom vakue for the key
- What is the parent template value?
