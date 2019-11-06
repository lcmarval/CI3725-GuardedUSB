
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTkPlusTkMinusleftTkMultTkDivTkModleftTkOrrightTkAndrightTkNotTkUminusleftTkOBracketTkCBracketnonassocTkLeqTkGeqTkEqualTkNEqualTkLessTkGreaterleftTkOpenParTkCloseParleftTkArrowTkAnd TkArray TkArrow TkAsig TkAtoi TkBool TkCBlock TkCBracket TkClosePar TkComma TkComments TkConcat TkDeclare TkDiv TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkPrintln TkPunto TkRead TkRof TkSemicolon TkSize TkSoForth TkString TkTo TkTrue TkTwoPoints TkUminusblock : TkOBlock TkCBlock\n\t| TkOBlock declare_variables instruction_block TkCBlock \n\t| TkOBlock instruction_block TkCBlock declare_variables : TkDeclare TkTwoPoints variable_List variable_List : TkId TkComma variable_List\n\t\t\t\t      | TkId TkTwoPoints type TkComma variable_List\n\t\t\t\t      | TkId TkTwoPoints type\n\t\t\t\t      | type TkComma variable_List\n\t\t\t\t      | type type : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket TkSemicolon\n\t| TkInt TkSemicolon\n\t| TkBool TkSemicolon\n\t| TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket\n\t| TkInt\n\t| TkBool instruction_block : instructions TkSemicolon instruction_block\n\t| instructions instructions : assign_inst\n\t| input_inst\n\t| output_inst\n\t| if_guard_inst\n\t| iteration_for_inst\n\t| iteration_do_inst\n\t| iteration_mult_guard_inst\n\t| block assign_inst : TkId TkAsig expressionarray_exp : TkId TkOpenPar expression TkTwoPoints expression TkClosePar array_exp \n\t| TkOpenPar expression TkTwoPoints expression TkClosePar array_exp\n\t| TkId TkOBracket expression TkCBracket\n\t| TkId TkConcat TkId\n\t| array_exp TkConcat TkId\n\t| TkId TkConcat array_exp\n\t| array_exp TkConcat array_exp\n\t| TkOBracket expression TkCBracket\n\t| TkAtoi TkOpenPar TkId TkClosePar\n\t| TkSize\n\t| TkMax\n\t| TkMin expression : TkOpenPar expression TkPlus expression TkClosePar\n\t| TkOpenPar expression TkMinus expression TkClosePar\n\t| TkOpenPar expression TkMult expression TkClosePar\n    | TkOpenPar expression TkDiv expression TkClosePar\n    | TkOpenPar expression TkMod expression TkClosePar\n    | TkOpenPar expression TkConcat expression TkClosePar\n    | TkOpenPar expression TkGeq expression TkClosePar\n    | TkOpenPar expression TkLess expression TkClosePar\n    | TkOpenPar expression TkGreater expression TkClosePar\n    | TkOpenPar expression TkNEqual expression TkClosePar\n    | TkOpenPar expression TkEqual expression TkClosePar\n    | TkOpenPar expression TkOr expression TkClosePar\n    | TkOpenPar expression TkAnd expression TkClosePar\n    | TkOpenPar TkUminus expression TkClosePar\n    | TkOpenPar TkNot expression TkClosePar\n    | TkOpenPar array_exp TkClosePar\n    | TkOpenPar TkId TkClosePar\n    | TkOpenPar TkNum TkClosePar\n    | TkOpenPar TkFalse TkClosePar\n    | TkOpenPar TkTrue TkClosePar\n    | TkOpenPar TkString TkClosePar  \n\t| expression TkPlus expression\n\t| expression TkMinus expression\n\t| expression TkMult expression\n\t| expression TkDiv expression\n\t| expression TkMod expression\n\t| expression TkLeq expression\n\t| expression TkGeq expression\n\t| expression TkLess expression\n\t| expression TkGreater expression\n\t| expression TkNEqual expression\n\t| expression TkEqual expression  \t\t   \n\t| expression TkOr expression\n\t| expression TkAnd expression\t   \n\t| TkUminus expression\n\t| TkNot expression\n\t| array_exp\n\t| TkId\n\t| TkNum\n\t| TkFalse\n\t| TkTrue\n\t| TkString   input_inst : TkRead TkId output_inst : TkPrint expression\n\t| TkPrintln expression if_guard_inst : TkIf expression TkArrow instructions if_guard_inst TkFi\n\t| TkGuard expression TkArrow instructions\n\tguards : TkGuard expression TkArrow instructions guards\n\t| TkGuard expression TkArrow instructions  iteration_for_inst : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof\n    iteration_do_inst : TkDo expression TkArrow instructions TkOd iteration_mult_guard_inst : TkDo expression TkArrow instructions guards TkOd\n\t| TkDo expression TkArrow instructions TkOd '
    
_lr_action_items = {'TkOBlock':([0,2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,202,203,204,208,],[2,2,2,2,-4,-9,-14,-15,2,2,2,-11,-12,-5,-7,-8,-6,2,2,-13,-10,]),'$end':([1,3,25,50,],[0,-1,-3,-2,]),'TkCBlock':([2,3,5,7,8,9,10,11,12,13,14,15,24,25,29,30,34,35,36,37,38,39,42,43,44,45,50,57,58,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,144,165,166,169,170,173,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,199,205,209,],[3,-1,25,-17,-18,-19,-20,-21,-22,-23,-24,-25,50,-3,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,-16,-26,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,-85,-52,-53,-29,-35,-89,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-28,-27,-88,]),'TkDeclare':([2,],[6,]),'TkId':([2,4,17,18,19,20,21,22,23,26,27,28,31,32,33,40,51,53,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,88,89,90,91,92,93,95,97,98,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,147,148,149,168,172,175,176,191,197,201,203,204,208,],[16,16,29,35,35,35,35,48,35,52,16,35,76,35,35,35,-4,-9,-14,-15,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,135,35,35,139,142,16,16,35,16,52,52,-11,-12,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-5,-7,-8,35,35,35,52,200,-6,200,16,-13,-10,]),'TkRead':([2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,203,204,208,],[17,17,17,-4,-9,-14,-15,17,17,17,-11,-12,-5,-7,-8,-6,17,-13,-10,]),'TkPrint':([2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,203,204,208,],[18,18,18,-4,-9,-14,-15,18,18,18,-11,-12,-5,-7,-8,-6,18,-13,-10,]),'TkPrintln':([2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,203,204,208,],[19,19,19,-4,-9,-14,-15,19,19,19,-11,-12,-5,-7,-8,-6,19,-13,-10,]),'TkIf':([2,3,4,8,9,10,11,12,13,14,15,25,27,29,30,34,35,36,37,38,39,42,43,44,45,50,51,53,55,56,58,81,82,89,90,92,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,143,144,147,148,149,165,166,169,170,173,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,197,199,203,204,205,208,209,],[20,-1,20,-18,-19,-20,-21,-22,-23,-24,-25,-3,20,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,-4,-9,-14,-15,-26,-73,-74,20,20,20,-11,-12,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,20,-85,-5,-7,-8,-52,-53,-29,-35,-89,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-6,-28,20,-13,-27,-10,-88,]),'TkGuard':([2,3,4,8,9,10,11,12,13,14,15,25,27,29,30,34,35,36,37,38,39,42,43,44,45,50,51,53,55,56,58,81,82,89,90,92,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,143,144,146,147,148,149,165,166,169,170,173,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,197,199,203,204,205,207,208,209,],[21,-1,21,-18,-19,-20,-21,-22,-23,-24,-25,-3,21,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,-4,-9,-14,-15,-26,-73,-74,21,21,21,-11,-12,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,21,-85,175,-5,-7,-8,-52,-53,-29,-35,-89,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-6,-28,21,-13,-27,175,-10,-88,]),'TkFor':([2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,203,204,208,],[22,22,22,-4,-9,-14,-15,22,22,22,-11,-12,-5,-7,-8,-6,22,-13,-10,]),'TkDo':([2,4,27,51,53,55,56,89,90,92,97,98,147,148,149,197,203,204,208,],[23,23,23,-4,-9,-14,-15,23,23,23,-11,-12,-5,-7,-8,-6,23,-13,-10,]),'TkSemicolon':([3,7,8,9,10,11,12,13,14,15,25,29,30,34,35,36,37,38,39,42,43,44,45,50,55,56,58,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,144,165,166,169,170,173,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,199,204,205,209,],[-1,27,-18,-19,-20,-21,-22,-23,-24,-25,-3,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,97,98,-26,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,-85,-52,-53,-29,-35,-89,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-28,208,-27,-88,]),'TkOd':([3,8,9,10,11,12,13,14,15,25,29,30,34,35,36,37,38,39,42,43,44,45,50,58,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,144,146,165,166,169,170,173,174,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,199,205,207,209,210,],[-1,-18,-19,-20,-21,-22,-23,-24,-25,-3,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,-26,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,-85,173,-52,-53,-29,-35,-89,195,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-28,-27,-87,-88,-86,]),'TkFi':([3,8,9,10,11,12,13,14,15,25,29,30,34,35,36,37,38,39,42,43,44,45,50,58,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,144,165,166,169,170,171,173,178,179,180,181,182,183,184,185,186,187,188,189,190,193,195,199,205,209,],[-1,-18,-19,-20,-21,-22,-23,-24,-25,-3,-81,-82,-75,-76,-77,-78,-79,-80,-36,-37,-38,-83,-2,-26,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,-85,-52,-53,-29,-35,193,-89,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-84,-90,-28,-27,-88,]),'TkRof':([3,25,50,206,],[-1,-3,-2,209,]),'TkTwoPoints':([6,34,35,36,37,38,39,42,43,44,52,72,75,76,77,78,79,80,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,139,140,141,151,152,153,154,155,157,158,159,160,161,162,163,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,199,205,],[26,-75,-76,-77,-78,-79,-80,-36,-37,-38,94,125,-75,-76,-77,-78,-79,-80,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,168,-30,-32,-34,-60,-61,-62,-63,-64,-66,-67,-68,-69,-70,-71,-72,-52,-53,125,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-28,-27,]),'TkAsig':([16,],[28,]),'TkOpenPar':([18,19,20,21,23,28,31,32,33,35,40,41,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,76,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,135,136,139,168,172,175,191,200,201,],[31,31,31,31,31,31,31,31,31,84,31,88,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,84,136,31,31,136,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,84,31,84,31,31,31,136,84,136,]),'TkUminus':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[32,32,32,32,32,32,73,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TkNot':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[33,33,33,33,33,33,74,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TkNum':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,96,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,177,],[36,36,36,36,36,36,77,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,150,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,198,]),'TkFalse':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[37,37,37,37,37,37,78,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TkTrue':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[38,38,38,38,38,38,79,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'TkString':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[39,39,39,39,39,39,80,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'TkOBracket':([18,19,20,21,23,28,31,32,33,35,40,54,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,76,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,135,136,139,168,172,175,191,200,201,],[40,40,40,40,40,40,40,40,40,85,40,96,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,85,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,85,40,85,40,40,40,40,85,40,]),'TkAtoi':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,191,201,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'TkSize':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,191,201,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'TkMax':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,191,201,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'TkMin':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,191,201,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'TkArray':([26,93,94,95,176,],[54,54,54,54,54,]),'TkInt':([26,93,94,95,176,],[55,55,55,55,55,]),'TkBool':([26,93,94,95,176,],[56,56,56,56,56,]),'TkPlus':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[59,-75,-76,-77,-78,-79,-80,-36,-37,-38,59,59,59,59,59,112,-75,-76,-77,-78,-79,-80,-73,-74,59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,59,59,-30,-32,-34,59,-60,-61,-62,-63,-64,59,-66,-67,-68,-69,-70,-71,-72,59,-52,-53,59,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,59,59,59,-28,-27,]),'TkMinus':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[60,-75,-76,-77,-78,-79,-80,-36,-37,-38,60,60,60,60,60,113,-75,-76,-77,-78,-79,-80,-73,-74,60,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,60,60,-30,-32,-34,60,-60,-61,-62,-63,-64,60,-66,-67,-68,-69,-70,-71,-72,60,-52,-53,60,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,60,60,60,-28,-27,]),'TkMult':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[61,-75,-76,-77,-78,-79,-80,-36,-37,-38,61,61,61,61,61,114,-75,-76,-77,-78,-79,-80,-73,-74,61,61,61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,61,61,-30,-32,-34,61,61,61,-62,-63,-64,61,-66,-67,-68,-69,-70,-71,-72,61,-52,-53,61,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,61,61,61,-28,-27,]),'TkDiv':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[62,-75,-76,-77,-78,-79,-80,-36,-37,-38,62,62,62,62,62,115,-75,-76,-77,-78,-79,-80,-73,-74,62,62,62,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,62,62,-30,-32,-34,62,62,62,-62,-63,-64,62,-66,-67,-68,-69,-70,-71,-72,62,-52,-53,62,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,62,62,62,-28,-27,]),'TkMod':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[63,-75,-76,-77,-78,-79,-80,-36,-37,-38,63,63,63,63,63,116,-75,-76,-77,-78,-79,-80,-73,-74,63,63,63,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,63,63,-30,-32,-34,63,63,63,-62,-63,-64,63,-66,-67,-68,-69,-70,-71,-72,63,-52,-53,63,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,63,63,63,-28,-27,]),'TkLeq':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[64,-75,-76,-77,-78,-79,-80,-36,-37,-38,64,64,64,64,64,64,-75,-76,-77,-78,-79,-80,64,64,64,64,64,64,64,64,None,None,None,None,None,None,64,64,64,64,-54,-55,-56,-57,-58,-59,-33,-31,64,64,-30,-32,-34,64,64,64,64,64,64,64,None,None,None,None,None,64,64,64,-52,-53,64,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,64,64,64,-28,-27,]),'TkGeq':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[65,-75,-76,-77,-78,-79,-80,-36,-37,-38,65,65,65,65,65,118,-75,-76,-77,-78,-79,-80,65,65,65,65,65,65,65,65,None,None,None,None,None,None,65,65,65,65,-54,-55,-56,-57,-58,-59,-33,-31,65,65,-30,-32,-34,65,65,65,65,65,65,65,None,None,None,None,None,65,65,65,-52,-53,65,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,65,65,65,-28,-27,]),'TkLess':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[66,-75,-76,-77,-78,-79,-80,-36,-37,-38,66,66,66,66,66,119,-75,-76,-77,-78,-79,-80,66,66,66,66,66,66,66,66,None,None,None,None,None,None,66,66,66,66,-54,-55,-56,-57,-58,-59,-33,-31,66,66,-30,-32,-34,66,66,66,66,66,66,66,None,None,None,None,None,66,66,66,-52,-53,66,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,66,66,66,-28,-27,]),'TkGreater':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[67,-75,-76,-77,-78,-79,-80,-36,-37,-38,67,67,67,67,67,120,-75,-76,-77,-78,-79,-80,67,67,67,67,67,67,67,67,None,None,None,None,None,None,67,67,67,67,-54,-55,-56,-57,-58,-59,-33,-31,67,67,-30,-32,-34,67,67,67,67,67,67,67,None,None,None,None,None,67,67,67,-52,-53,67,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,67,67,67,-28,-27,]),'TkNEqual':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[68,-75,-76,-77,-78,-79,-80,-36,-37,-38,68,68,68,68,68,121,-75,-76,-77,-78,-79,-80,68,68,68,68,68,68,68,68,None,None,None,None,None,None,68,68,68,68,-54,-55,-56,-57,-58,-59,-33,-31,68,68,-30,-32,-34,68,68,68,68,68,68,68,None,None,None,None,None,68,68,68,-52,-53,68,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,68,68,68,-28,-27,]),'TkEqual':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[69,-75,-76,-77,-78,-79,-80,-36,-37,-38,69,69,69,69,69,122,-75,-76,-77,-78,-79,-80,69,69,69,69,69,69,69,69,None,None,None,None,None,None,69,69,69,69,-54,-55,-56,-57,-58,-59,-33,-31,69,69,-30,-32,-34,69,69,69,69,69,69,69,None,None,None,None,None,69,69,69,-52,-53,69,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,69,69,69,-28,-27,]),'TkOr':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[70,-75,-76,-77,-78,-79,-80,-36,-37,-38,70,70,70,70,70,123,-75,-76,-77,-78,-79,-80,-73,-74,70,70,70,70,70,70,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,70,70,-30,-32,-34,70,70,70,70,70,70,70,-66,-67,-68,-69,-70,-71,-72,70,-52,-53,70,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,70,70,70,-28,-27,]),'TkAnd':([30,34,35,36,37,38,39,42,43,44,45,46,47,49,58,72,75,76,77,78,79,80,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,194,196,199,205,],[71,-75,-76,-77,-78,-79,-80,-36,-37,-38,71,71,71,71,71,124,-75,-76,-77,-78,-79,-80,-73,-74,71,71,71,71,71,71,-65,-66,-67,-68,-69,-70,71,71,-73,-74,-54,-55,-56,-57,-58,-59,-33,-31,71,71,-30,-32,-34,71,71,71,71,71,71,71,-66,-67,-68,-69,-70,71,71,71,-52,-53,71,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,71,71,71,-28,-27,]),'TkArrow':([34,35,36,37,38,39,42,43,44,46,47,49,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,165,166,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,194,196,199,205,],[-75,-76,-77,-78,-79,-80,-36,-37,-38,89,90,92,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,-52,-53,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,202,203,-28,-27,]),'TkCBracket':([34,35,36,37,38,39,42,43,44,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,138,139,140,141,165,166,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,198,199,205,],[-75,-76,-77,-78,-79,-80,-36,-37,-38,-73,-74,141,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,169,-30,-32,-34,-52,-53,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,204,-28,-27,]),'TkConcat':([34,35,36,37,38,39,42,43,44,72,75,76,77,78,79,80,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,139,140,141,151,152,153,154,155,157,158,159,160,161,162,163,165,166,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,199,200,205,],[83,86,-77,-78,-79,-80,-36,-37,-38,117,83,86,-77,-78,-79,-80,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-54,-55,-56,-57,-58,-59,83,86,86,83,-34,-60,-61,-62,-63,-64,-66,-67,-68,-69,-70,-71,-72,-52,-53,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-28,86,-27,]),'TkClosePar':([34,35,36,37,38,39,42,43,44,75,76,77,78,79,80,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,128,129,130,131,132,133,134,135,139,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,192,199,205,],[-75,-76,-77,-78,-79,-80,-36,-37,-38,128,129,130,131,132,133,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,165,166,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,170,178,179,180,181,182,183,184,185,186,187,188,189,190,191,-52,-53,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,201,-28,-27,]),'TkTo':([34,35,36,37,38,39,42,43,44,81,82,99,100,101,102,103,104,105,106,107,108,109,110,111,128,129,130,131,132,133,134,135,139,140,141,145,165,166,169,170,178,179,180,181,182,183,184,185,186,187,188,189,190,199,205,],[-75,-76,-77,-78,-79,-80,-36,-37,-38,-73,-74,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-54,-55,-56,-57,-58,-59,-33,-31,-30,-32,-34,172,-52,-53,-29,-35,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-28,-27,]),'TkIn':([48,],[91,]),'TkComma':([52,53,55,56,97,98,148,204,208,],[93,95,-14,-15,-11,-12,176,-13,-10,]),'TkSoForth':([150,],[177,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,2,4,27,89,90,92,202,203,],[1,15,15,15,15,15,15,206,15,]),'declare_variables':([2,],[4,]),'instruction_block':([2,4,27,],[5,24,57,]),'instructions':([2,4,27,89,90,92,203,],[7,7,7,143,144,146,207,]),'assign_inst':([2,4,27,89,90,92,203,],[8,8,8,8,8,8,8,]),'input_inst':([2,4,27,89,90,92,203,],[9,9,9,9,9,9,9,]),'output_inst':([2,4,27,89,90,92,203,],[10,10,10,10,10,10,10,]),'if_guard_inst':([2,4,27,89,90,92,143,203,],[11,11,11,11,11,11,171,11,]),'iteration_for_inst':([2,4,27,89,90,92,203,],[12,12,12,12,12,12,12,]),'iteration_do_inst':([2,4,27,89,90,92,203,],[13,13,13,13,13,13,13,]),'iteration_mult_guard_inst':([2,4,27,89,90,92,203,],[14,14,14,14,14,14,14,]),'expression':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,84,85,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,],[30,45,46,47,49,58,72,81,82,87,99,100,101,102,103,104,105,106,107,108,109,110,111,126,127,137,138,145,151,152,153,154,155,156,157,158,159,160,161,162,163,164,167,192,194,196,]),'array_exp':([18,19,20,21,23,28,31,32,33,40,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,83,84,85,86,91,112,113,114,115,116,117,118,119,120,121,122,123,124,125,136,168,172,175,191,201,],[34,34,34,34,34,34,75,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,134,34,34,140,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,199,205,]),'variable_List':([26,93,95,176,],[51,147,149,197,]),'type':([26,93,94,95,176,],[53,53,148,53,53,]),'guards':([146,207,],[174,210,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> TkOBlock TkCBlock','block',2,'p_block','parser.py',70),
  ('block -> TkOBlock declare_variables instruction_block TkCBlock','block',4,'p_block','parser.py',71),
  ('block -> TkOBlock instruction_block TkCBlock','block',3,'p_block','parser.py',72),
  ('declare_variables -> TkDeclare TkTwoPoints variable_List','declare_variables',3,'p_declare_variables','parser.py',84),
  ('variable_List -> TkId TkComma variable_List','variable_List',3,'p_variable_List','parser.py',89),
  ('variable_List -> TkId TkTwoPoints type TkComma variable_List','variable_List',5,'p_variable_List','parser.py',90),
  ('variable_List -> TkId TkTwoPoints type','variable_List',3,'p_variable_List','parser.py',91),
  ('variable_List -> type TkComma variable_List','variable_List',3,'p_variable_List','parser.py',92),
  ('variable_List -> type','variable_List',1,'p_variable_List','parser.py',93),
  ('type -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket TkSemicolon','type',7,'p_type','parser.py',107),
  ('type -> TkInt TkSemicolon','type',2,'p_type','parser.py',108),
  ('type -> TkBool TkSemicolon','type',2,'p_type','parser.py',109),
  ('type -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket','type',6,'p_type','parser.py',110),
  ('type -> TkInt','type',1,'p_type','parser.py',111),
  ('type -> TkBool','type',1,'p_type','parser.py',112),
  ('instruction_block -> instructions TkSemicolon instruction_block','instruction_block',3,'p_instruction_block','parser.py',129),
  ('instruction_block -> instructions','instruction_block',1,'p_instruction_block','parser.py',130),
  ('instructions -> assign_inst','instructions',1,'p_instructions','parser.py',138),
  ('instructions -> input_inst','instructions',1,'p_instructions','parser.py',139),
  ('instructions -> output_inst','instructions',1,'p_instructions','parser.py',140),
  ('instructions -> if_guard_inst','instructions',1,'p_instructions','parser.py',141),
  ('instructions -> iteration_for_inst','instructions',1,'p_instructions','parser.py',142),
  ('instructions -> iteration_do_inst','instructions',1,'p_instructions','parser.py',143),
  ('instructions -> iteration_mult_guard_inst','instructions',1,'p_instructions','parser.py',144),
  ('instructions -> block','instructions',1,'p_instructions','parser.py',145),
  ('assign_inst -> TkId TkAsig expression','assign_inst',3,'p_assign_inst','parser.py',150),
  ('array_exp -> TkId TkOpenPar expression TkTwoPoints expression TkClosePar array_exp','array_exp',7,'p_array_exp','parser.py',155),
  ('array_exp -> TkOpenPar expression TkTwoPoints expression TkClosePar array_exp','array_exp',6,'p_array_exp','parser.py',156),
  ('array_exp -> TkId TkOBracket expression TkCBracket','array_exp',4,'p_array_exp','parser.py',157),
  ('array_exp -> TkId TkConcat TkId','array_exp',3,'p_array_exp','parser.py',158),
  ('array_exp -> array_exp TkConcat TkId','array_exp',3,'p_array_exp','parser.py',159),
  ('array_exp -> TkId TkConcat array_exp','array_exp',3,'p_array_exp','parser.py',160),
  ('array_exp -> array_exp TkConcat array_exp','array_exp',3,'p_array_exp','parser.py',161),
  ('array_exp -> TkOBracket expression TkCBracket','array_exp',3,'p_array_exp','parser.py',162),
  ('array_exp -> TkAtoi TkOpenPar TkId TkClosePar','array_exp',4,'p_array_exp','parser.py',163),
  ('array_exp -> TkSize','array_exp',1,'p_array_exp','parser.py',164),
  ('array_exp -> TkMax','array_exp',1,'p_array_exp','parser.py',165),
  ('array_exp -> TkMin','array_exp',1,'p_array_exp','parser.py',166),
  ('expression -> TkOpenPar expression TkPlus expression TkClosePar','expression',5,'p_expression','parser.py',186),
  ('expression -> TkOpenPar expression TkMinus expression TkClosePar','expression',5,'p_expression','parser.py',187),
  ('expression -> TkOpenPar expression TkMult expression TkClosePar','expression',5,'p_expression','parser.py',188),
  ('expression -> TkOpenPar expression TkDiv expression TkClosePar','expression',5,'p_expression','parser.py',189),
  ('expression -> TkOpenPar expression TkMod expression TkClosePar','expression',5,'p_expression','parser.py',190),
  ('expression -> TkOpenPar expression TkConcat expression TkClosePar','expression',5,'p_expression','parser.py',191),
  ('expression -> TkOpenPar expression TkGeq expression TkClosePar','expression',5,'p_expression','parser.py',192),
  ('expression -> TkOpenPar expression TkLess expression TkClosePar','expression',5,'p_expression','parser.py',193),
  ('expression -> TkOpenPar expression TkGreater expression TkClosePar','expression',5,'p_expression','parser.py',194),
  ('expression -> TkOpenPar expression TkNEqual expression TkClosePar','expression',5,'p_expression','parser.py',195),
  ('expression -> TkOpenPar expression TkEqual expression TkClosePar','expression',5,'p_expression','parser.py',196),
  ('expression -> TkOpenPar expression TkOr expression TkClosePar','expression',5,'p_expression','parser.py',197),
  ('expression -> TkOpenPar expression TkAnd expression TkClosePar','expression',5,'p_expression','parser.py',198),
  ('expression -> TkOpenPar TkUminus expression TkClosePar','expression',4,'p_expression','parser.py',199),
  ('expression -> TkOpenPar TkNot expression TkClosePar','expression',4,'p_expression','parser.py',200),
  ('expression -> TkOpenPar array_exp TkClosePar','expression',3,'p_expression','parser.py',201),
  ('expression -> TkOpenPar TkId TkClosePar','expression',3,'p_expression','parser.py',202),
  ('expression -> TkOpenPar TkNum TkClosePar','expression',3,'p_expression','parser.py',203),
  ('expression -> TkOpenPar TkFalse TkClosePar','expression',3,'p_expression','parser.py',204),
  ('expression -> TkOpenPar TkTrue TkClosePar','expression',3,'p_expression','parser.py',205),
  ('expression -> TkOpenPar TkString TkClosePar','expression',3,'p_expression','parser.py',206),
  ('expression -> expression TkPlus expression','expression',3,'p_expression','parser.py',207),
  ('expression -> expression TkMinus expression','expression',3,'p_expression','parser.py',208),
  ('expression -> expression TkMult expression','expression',3,'p_expression','parser.py',209),
  ('expression -> expression TkDiv expression','expression',3,'p_expression','parser.py',210),
  ('expression -> expression TkMod expression','expression',3,'p_expression','parser.py',211),
  ('expression -> expression TkLeq expression','expression',3,'p_expression','parser.py',212),
  ('expression -> expression TkGeq expression','expression',3,'p_expression','parser.py',213),
  ('expression -> expression TkLess expression','expression',3,'p_expression','parser.py',214),
  ('expression -> expression TkGreater expression','expression',3,'p_expression','parser.py',215),
  ('expression -> expression TkNEqual expression','expression',3,'p_expression','parser.py',216),
  ('expression -> expression TkEqual expression','expression',3,'p_expression','parser.py',217),
  ('expression -> expression TkOr expression','expression',3,'p_expression','parser.py',218),
  ('expression -> expression TkAnd expression','expression',3,'p_expression','parser.py',219),
  ('expression -> TkUminus expression','expression',2,'p_expression','parser.py',220),
  ('expression -> TkNot expression','expression',2,'p_expression','parser.py',221),
  ('expression -> array_exp','expression',1,'p_expression','parser.py',222),
  ('expression -> TkId','expression',1,'p_expression','parser.py',223),
  ('expression -> TkNum','expression',1,'p_expression','parser.py',224),
  ('expression -> TkFalse','expression',1,'p_expression','parser.py',225),
  ('expression -> TkTrue','expression',1,'p_expression','parser.py',226),
  ('expression -> TkString','expression',1,'p_expression','parser.py',227),
  ('input_inst -> TkRead TkId','input_inst',2,'p_input_inst','parser.py',231),
  ('output_inst -> TkPrint expression','output_inst',2,'p_output_inst','parser.py',235),
  ('output_inst -> TkPrintln expression','output_inst',2,'p_output_inst','parser.py',236),
  ('if_guard_inst -> TkIf expression TkArrow instructions if_guard_inst TkFi','if_guard_inst',6,'p_if_guard_inst','parser.py',240),
  ('if_guard_inst -> TkGuard expression TkArrow instructions','if_guard_inst',4,'p_if_guard_inst','parser.py',241),
  ('guards -> TkGuard expression TkArrow instructions guards','guards',5,'p_guards','parser.py',248),
  ('guards -> TkGuard expression TkArrow instructions','guards',4,'p_guards','parser.py',249),
  ('iteration_for_inst -> TkFor TkId TkIn expression TkTo expression TkArrow block TkRof','iteration_for_inst',9,'p_iteration_for_inst','parser.py',256),
  ('iteration_do_inst -> TkDo expression TkArrow instructions TkOd','iteration_do_inst',5,'p_iteration_do_inst','parser.py',261),
  ('iteration_mult_guard_inst -> TkDo expression TkArrow instructions guards TkOd','iteration_mult_guard_inst',6,'p_iteration_mult_guard_inst','parser.py',265),
  ('iteration_mult_guard_inst -> TkDo expression TkArrow instructions TkOd','iteration_mult_guard_inst',5,'p_iteration_mult_guard_inst','parser.py',266),
]