HR.appController.addTemplate("backbone/templates/recruit/topbar",function(obj){{var __t,__p="";Array.prototype.join}with(obj||{})__p+='<header class="nav-make-fixed min-1024 ',test.get("logo")&&(__p+=" hr_haslogo "),__p+='" id="page-header">\n    <div class="row-fluid">\n        ',test.get("logo")?(__p+='\n        <span class="span6 nav-logo">\n            <a class="HackerRankLogo backbone company-logo-candidate-site"><!--?xml version=\'1.0\' encoding=\'utf-8\'?--><!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n                <img src="'+(null==(__t=test.get("logo"))?"":__t)+'" />\n                <!-- <img class="toploader hidden" src="https://hrcdn.net/hackerrank/assets/ajax-msg-loader-4d8e554413e48d07592e67c5d804a2c1.gif" style="position: absolute;top: 23px;left: 68px;"> -->\n            </a>\n            <span style="padding-left:50px;" class="text-ellipsis txt-white customer-font-color mlA">'+(null==(__t=test.get("name"))?"":_.escape(__t))+"\n            ",test.get("multi_login").length>0&&(__p+='\n              <a class="js-othertest mlL" href=""><small>(other)</small> <i class="icon--single icon-ellipsis"></i></a>\n            '),__p+="\n            </span>\n        </span>\n        "):(__p+='\n        <div class="span6">\n            <span class="nav-logo"><a class="HackerRankLogo backbone logo-candidate-site"><!--?xml version=\'1.0\' encoding=\'utf-8\'?--><!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n                <img src="/assets/brand/h_mark_sm.png" /></a>\n                <!-- <img class="toploader hidden" src="https://hrcdn.net/hackerrank/assets/ajax-msg-loader-4d8e554413e48d07592e67c5d804a2c1.gif" style="position: absolute;top: 23px;left: 68px;"> -->\n            </span>\n            <span style="padding-left:50px;" class="text-ellipsis txt-white customer-font-color mlA">'+(null==(__t=test.get("name"))?"":_.escape(__t))+"\n            ",test.get("multi_login").length>0&&(__p+='\n              <a class="js-othertest mlL" href=""><small>(other)</small> <i class="icon--single icon-ellipsis"></i></a>\n            '),__p+="\n            </span>\n        </div> <!-- .span7 -->\n        "),__p+='\n\n        <div class="span2 text-center">\n            <div class="pmT pmB mmT mmB timerspan ',showalert&&(__p+="alerttimer"),__p+='"><i class="icon-clock txt-alt-grey"></i>&nbsp;<span class="txt-white customer-font-color fnt-sz-mid" id="countdown-timer"></span><br><span class="timer-tag customer-font-color" id="timertag"></span></div>\n        </div> <!-- .span3 -->\n        <div class="span1">&nbsp;</div>\n\n        <div class="span4">\n            <div class="mlT txt-white customer-font-color fnt-sz-mid">\n                <div class="dark-theme-progress small">\n                    <div class="base">\n                        <div class="cover progress-done"></div>\n                    </div>\n                </div>\n                &nbsp;<span class="qdone"></span>/<span class="qcount"></span> Attempted\n            </div>\n        </div> <!-- .span4 -->\n\n        <div class="span3">\n            <span class="text-ellipsis txt-white customer-font-color mlT"><i class="icon-user txt-alt-grey fnt-sz-mid"></i>&nbsp;'+(null==(__t=attempt.get("email"))?"":_.escape(__t))+"</span>\n        </div> <!-- .span2 -->\n\n    </div> <!-- .row-fluid -->\n</header>\n\n";return __p});