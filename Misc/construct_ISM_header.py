#
from InternetWireFormatISM import Internet_Wire_Format_ISM
from Nat import Nat

def construct_ISM_header(): 
    
    with Internet_Wire_Format_ISM() as ISM:
        # 6.1 Table3 Registers Summary first page of table (Page 60)
        ISM.field("RegFifo",0x00,Nat,8,"FIFO read/write access") #
        ISM.field("RegOpMode",0x04,Nat,8,"Operating modes of the transceiver") # 
        ISM.field("RegDataModul",0x00,Nat,8,"Data operation mode and Modulation settings") # 
        ISM.field("RegBitrate",0x1A0B,Nat,16,"Bit Rate setting") # RegBitrateMsb,RegBitrateLsb
        ISM.field("RegFdev",0x0052,Nat,16,"Frequency Deviation Setting") # RegFdevMsb, RegFdevLsb
        ISM.field("RegFrf",0xE4C000,Nat,24,"RF Carrier Frequency") # RegFrfMsb, RegFrfMid, RegFrfLsb
        ISM.field("RegOsc1",0x41,Nat,8,"RC Oscillators Settings")
        ISM.field("RegAfcCtrl",0x00,Nat,8,"AFC control in low modulation index situations") #
        ISM.field("Regserved0C",0x02,Nat,8,"-") #
        ISM.field("RegListen1",0x92,Nat,8,"Listen Mode settings") # 
        ISM.field("RegListen2",0xF5,Nat,8,"Listen Mode Idle duration") #
        ISM.field("RegListen3",0x20,Nat,8,"Listen Mode Rx duration") #  
        ISM.field("RegVersion",0x24,Nat,8,"") #  
        ISM.field("RegPALevel",0x9F,Nat,8,"PA selection and Output Power control")
        ISM.field("RegPARamp",0x09,Nat,8,"Control of the PA ramp time in FSK mode") #
        ISM.field("RegOcp",0x1A,Nat,8,"Over Current Protection control") # 
        ISM.field("Reserved14",0x40,Nat,8,"-") # 
        ISM.field("Reserved15",0x80,Nat,8,"-") # 
        ISM.field("Reserved16",0x7B,Nat,8,"-") # 
        ISM.field("Reserved17",0x9B,Nat,8,"-") # 
        ISM.field("RegLna",0x8B,Nat,8,"LNA Settings")
        ISM.field("RegRxBw",0x55,Nat,8,"Channel Filter BW Control") #
        # 6.1 Table3 Registers Summary second page of table (Page 61)
        ISM.field("RegAfcBw",0x8B,Nat,8,"Channel Filter BW control during the AFC routine") #
        ISM.field("RegOokPeak",0x40,Nat,8,"OOK demodulator selection and control in peak mode") # 
        ISM.field("RegOokFix",0xF5,Nat,8,"Fixed threshold control of the OOK demodulator") #
        ISM.field("RegAfcFei",0x10,Nat,8,"AFC and FEI control and status") #  
        ISM.field("RegRssiConfig",0x02,Nat,8,"RSSI-related settings") #  RegFeiMsb , RegFeiLsb
        ISM.field("RegRssiValue",0xFF,Nat,8,"RSSI value in dBm") #
        ISM.field("RegDioMapping1",0x00,Nat,8,"Map of pins DIO0 to DIO3") #
        ISM.field("RegDioMapping2",0x07,Nat,8,"Map of pins DIO4 and DIO5, ClkOut frequency") #  
        ISM.field("RegirqFlags1",0x80,Nat,8,"") #  
        ISM.field("RegirqFlags2",0x00,Nat,8,"PA selection and Output Power control")
        ISM.field("RegRssiThresh",0xE4,Nat,8,"RSSI Threshold control") #
        ISM.field("RegRxTimeout1",0x00,Nat,8,"Timeout duration between Rx request and RSSi detection") # 
        ISM.field("RegRxTimeout2",0x00,Nat,8,"Timeout duration between RSSi detection and PayloadReady request and RSSi detection") # 
        ISM.field("RegPreamble",0x0093,Nat,16,"Preamble length") # RegPreambleLsb, RegPreambleMsb
        ISM.field("RegSyncConfig",0x01,Nat,8,"Synch Word Recognition control") # 
        ISM.field("RegSyncValue1-8",0x01,Nat,8,"Synch Word bytes, 1 trough 8") # 
        ISM.field("RegPacketConfig1",0x10,Nat,8,"Packet mode settings") #
        ISM.field("RegPayloadLength",0x40,Nat,8,"Payload length setting") #
        ISM.field("RegNodeAdrs",0x00,Nat,8,"Node address") #
        ISM.field("RegBroadcastAdrs",0x40,Nat,8,"Broadcast address") #
        ISM.field("RegAutoModes",0x00,Nat,8,"Auto modes settings") #
        ISM.field("RegFifoThresh",0x8F,Nat,8,"Fifo threshold, Tx start condition")
        ISM.field("RegPacketConfig2",0x02,Nat,8,"Packet mode settings")
        # 6.1 Table3 Registers Summary tnird page of table (Page 62)
        ISM.field("RegAesKey1-16",0,Nat,8*16,"(The) 16 bytes of the cypher key")
        ISM.field("RegTemp1",0x01,Nat,8,"Temperature Sensor control")
        ISM.field("RegTemp2",0x00,Nat,8,"Temperature readout")
        ISM.field("RegTestPa1",0x01,Nat,8,"High Power PA settings")
        ISM.field("RegTestPa2",0x00,Nat,8,"Fading margin improvement")
        ISM.field("RegTestAfc",0x00,Nat,8,"AFC offset for low modulation index AFC")
        ISM.field("RegTest",0x00,Nat,8,"Internal test registers")
         
    return ISM

ISM = construct_ISM_header()
#ISM.data_octets.data_value = 123456
#ISM.Source_Port.data_value=0x11
#ISM.Destination_Port.data_value=5280 # Layer4.TransientPort()
#ISM.Length = ISM.data_octets.data_value.bit_length()
print(ISM)
##    ISM.NextProtocolValue = 33
##    print(ISM_Header.NextProtocol)
##    
    
print("implementation version 2ISM.py")
     
  
