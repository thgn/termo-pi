# termo-pi

This project goal is to make a rasperry pi controlled heating system using raspberry pi.

The scheme is:



 -----------

|termostato |

|           |   ----WiFi--------

|           |                   |

|           |                   |

|           |                   |

 -----------                    1 -----> -----------

	|			|	|termo-rele1|

	|			|	|           |

	|			|	| Relay     |

	|			|	|Thermometer|

	|			|	|           |

Internet			|	 -----------

				|

				|

				|

				2 -----> -----------

				|	|termo-rele2|

				|	|           |

				|	| Relay     |

				|	|Thermometer|

				|	|           |

				|	 -----------

				X

				X

				N -----> -----------

					|termo-releN|

					|           |

					| Relay     |

					|Thermometer|

					|           |

					 -----------



