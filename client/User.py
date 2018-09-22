# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:25:53 2018

Script to generate basic data insights 
involving connections and revenue
(mostly made to help form ideas
for our app)

@author: kevin
"""
from collections import Counter

class User:
    def __init__(self, name, connections, donationAmt):
        self.name = name
        self.connections = connections
        self.donationAmt = donationAmt
        
    def getGroupRevenue(self):
        """
        Get revenue a particular user's 
        group generates
        """
        return self.donationAmt +  sum([connection.donationAmt for connection
                                        in self.connections])
    
    def getSecondDegreeConnections(self):
        """
        Identify sets of users a given user
        may know through user's first-degree
        connections
        """
        return [set(connection.connections) - set(self.connections) 
                for connection in self.connections]
    
    def mostCommonSecondDegreeConnection(self):
        """
        Identify users that a given user 
        is likeliest to already know through
        first-degree connections and provides number of
        mutual connections between a user and another
        """
        sdcGroups = self.getSecondDegreeConnections()
        sdcs = []
        
        for group in sdcGroups:
            sdcs.extend(list(group))
        
        return Counter(sdcs).most_common()  
        
    def sortConnectionsByDonationAmt(self):
        """
        Sorts connections in ascending order by 
        their donation amounts
        """
        return sorted(self.connections, key=lambda x: x.donationAmt)
    

            
    
        
        
        
        
        
        
        
        
        
        
        
        
