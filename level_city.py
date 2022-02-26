import pygame, sys

level_city_map =[
'                                                                       SSSS                   ',
'                                                          SSSSSSS                             ',
'                                                                              XX        XX    ',
'                                                                    B         XX      SSXX    ',
'                                                              B S       B     XX        XX    ',
'                                                         S     S       XXX    XXSS      XX    ',
'                                                         S                    XX       SXX    ',
'                                                           B         SSSSSSSSSXXSS      XX    ',
'                                                               B              XX        XX    ',
'                                                                S    S        XX   SS   XX    ',
'                                                                S             XX        XX    ',
'                                                                   B      SSS XX      SSXX    ',
'                                                                          S   XX        XX    ',
'                                                           R  S         B S   XXS       XX    ',
'                                                          XXXXXXX             XX   S   SXX    ',
'                                                          XXXXXXX             XX        XX    ',
'                                            XX         M  XXXXXXX       B     XXS       XX    ',
'P                C                       R      R         XXXXXXX             XX       SXX    ',
'XXXXXX  XX  XX  XX   XX               XXXXXXXXXXXXXX     BXXXXXXX         B   XX   SS   XX    ',
'XXXXXXXXXXXXXXXXXX        XX          XXXXXXXXXXXXXX      XXXXXXX      B      XX            E ',
'XXXXXXXXXXXXXXXXXX  XX          AAAA  XXXXXXXXXXXXXX      XXXXXXX  B          XXXXXXXXXXXXXXX ',
'XXXXXXXXXXXXXXXXXX       XX           XXXXXXXXXXXXXX      XXXXXXX             XXXXXXXXXXXXXXX ',
'XXXXXXXXXXXXXXXXXXSSSSSSSSSSSSSSSSSSSSXXXXXXXXXXXXXXSSSSSSXXXXXXXSSSSSSSSSSSSSXXXXXXXXXXXXXXX '
]

#A = awning sprite (bouncy pad)
#B = boost pad
#X = tiles
#P = player
#E = level end
#R = rat sprite (spike)
#M = moving platform