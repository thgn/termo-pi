# termo-pi

This project goal is to make a rasperry pi controlled heating system using raspberry pi.

The scheme is:



 ___________
|termostato |

|           |   ____WiFi________

|           |                   |

|           |                   |

|___________|                   |
 
                                1======>
                                         ___________
	|			|	|termo-rele1|

	|			|	|           |

	|			|	| Relay     |

	|			|	|Thermometer|

	|			|	|___________|

Internet			|

				|

				|

				|

				2======>
					 ___________
				|	|termo-rele2|

				|	|           |

				|	| Relay     |

				|	|Thermometer|

				|	|___________|
									
				X

				X

				N ======>
					 ___________
					|termo-releN|

					|           |

					| Relay     |

					|Thermometer|

					|___________|




