import pygame, sys
from settings import *

level_tutorial_map = [
'                                                                       ',
'                                                                       ',
'          XX                                             X             ',
'          XX                  B         B           B    XX            ',
'          XX       XX                                    XXX           ',
'          XX   X          B     B                        XXXX          ',
'          XXXXXXXXXXXXXXXXX    XXX   B  XXX              XXXXX         ',
'          XXXXXXXXXXXXXXXXXXXXXXXX      XXX   B          XXXXXX        ',
'                                                      B  XXXXXXX       ',
'                                                         XXXXXXXX      ',
'                        XXX     XXX                      XXXXXXXXX     ',
'         S    XXXX  XX      XX      XX   XXXXXX     B    XXXXXXXXXX    ',
'   P XXXXXXXXXXXXX          XX           XXXXXXXX        XXXXXXXXXXX E ',
' XXXXXXXXXXXXXXXXXSSSSSSSSSSXXSSSSSSSSSSSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_height = tile_size * len(level_tutorial_map)