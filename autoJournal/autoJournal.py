class OrderStatus:

    def __init__(self):
        self.LocalTime = ""
        self.MarketDateTime = ""
        self.Currency = ""
        self.Symbol = ""
        self.Gateway = ""
        self.Side = ""
        self.OrderNumber = ""
        self.Price = ""
        self.Shares = ""
        self.Position = ""
        self.OrderState = ""
        self.MarketId = ""
        self.CurrencyChargeGway = ""
        self.ChargeGway = ""
        self.CurrencyChargeAct = ""
        self.ChargeAct = ""
        self.CurrencyChargeSec = ""
        self.ChargeSec = ""
        self.CurrencyChargeExec = ""
        self.ChargeExec = ""
        self.CurrencyChargeClr = ""
        self.ChargeClr = ""
        self.OrderFlags = ""
        self.CurrencyCharge = ""
        self.Account = ""
        self.InfoCode = ""
        self.InfoText = ""
        self.OrderStatus = {}

    def update(self, symbol, localtime, msgtime, side, price, shares, position, order_state, order_flags):
        msg = {}
        msg['LocalTime'] = localtime
        msg['MarketDataTime'] = msgtime
        msg['Symbol'] = symbol
        msg['Side'] = side
        msg['Price'] = price
        msg['Shares'] = shares
        msg['Position'] = position
        msg['OrderState'] = order_state
        msg['OrderFlags'] = order_flags
        print("Processing Order Status Message")
        self.OrderStatus[symbol + msgtime] = msg

class OrderEvenets:

    def __init__(self):
        self.LocalTime = ""
        self.Message = ""
        self.MarketDataTime = ""
        self.OrderNumber = ""
        self.OriginatorSeqId = ""
        self.EventMessageType = ""
        self.EventFlavour = ""
        self.EventOriginatorId = ""
        self.Price = ""
        self.Size = ""
        self.Description = ""
        self.OrderEvent = {}

    def update(self, localtime, msg, msgtime, ordnum, origintorseqid, eventmsgtype, eventflavour, eventoriginatorid, price, size, description):
        msg = {}
        msg['LocalTime'] = localtime
        msg['Message'] = msg
        msg['MarketDataTime'] = msgtime
        msg['OrderNumber'] = ordnum
        msg['EventMessageType'] = eventmsgtype
        msg['EventFlavour'] = eventflavour
        msg['EventOriginatorId'] = eventoriginatorid
        msg['Size'] = size
        msg['Price'] = price
        msg['Description'] = description
        print("Processing Order Event Message")
        self.OrderEvent[origintorseqid] = msg

    def get_events(self):
        for key, event in self.OrderEvent.items():
            print(key, event)

    def getOrder(self, ordernumber):
        for key, orderevent in self.OrderEvent.items():
            if orderevent['EventFlavour'] == '2' and orderevent['OrderNumber'] == ordernumber:
                return orderevent

    def isorderfilled(self, ordernumber):
        for key, orderevent in self.OrderEvent.items():
            # EventFlavour = 2 = Accepted
            if orderevent['EventFlavour'] == '4' and orderevent['OrderNumber'] == ordernumber:
                return orderevent

