import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, customer: str, issue: str) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        raise NotImplementedError


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy().reverse()



class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer: str, issue: str) -> None:
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


def main():

    app = CustomerSupport()

    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")

    app.process_tickets(FIFOOrderingStrategy())


if __name__ == '__main__':
    main()
