HR.appController.addTemplate("backbone/templates/recruit/question-base",function(obj){{var __t,__p="";Array.prototype.join}with(obj||{})__p+='<div class="container" style="margin-top:63px; ">\n    <div class="title-name-wrapper">\n        <!--a class="backbone" href='+(null==(__t="/tests/"+tid+"/questions")?"":__t)+' >&lt; Back to list</a>\n    <div class="clear"></div-->\n        <h1 class="title pull-left qtitle"></h1>\n        <h4 class="bold pull-right qpoints"></h4>\n        <div class="clear"></div>\n    </div>\n    <div class="container--inner">\n      ',"task"!=question.type?(__p+='\n        <div class="span11 challenge-text hrx-version ck_table-wrap">\n        </div><!-- end challenge-text -->\n        <div class="clear"></div>\n        <div class="soft-divider mlB"></div>\n        ',"code"==question.type&&(__p+='\n        <div class="mlB"><h4>YOUR ANSWER</h4></div>\n        '),__p+='\n        <div class="qcontent">\n        </div>\n        <div class="clear"></div>\n        ',-1==$.inArray(question.type,["code","approx","design","code_upload","project"])&&(__p+='\n        <button class="btn btn-primary mdT mdB mdR ans-submit" style="width:225px;">Submit answer & continue</button>\n        '),__p+="\n      "):__p+='\n        <div class="qcontent">\n        </div>\n      ',__p+="\n    </div><!-- end container-inner -->\n</div> <!-- end .container -->\n";return __p});