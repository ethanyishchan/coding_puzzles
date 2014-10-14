HR.appController.addTemplate("backbone/templates/recruit/question-servertask",function(obj){{var __t,__p="";Array.prototype.join}with(obj||{})__p+='<div class="span-xs-16 span-md-4 task-sidebar pdA js-sidebar-holder">\n ',null==question.solve?__p+='\n   <p>This is a server type task, and you will complete a set of tasks on a live Linux server.</p>\n   <p class="pdT">All activity will be monitored. Access to the server is being provided <em>only</em> to complete tasks, and nothing else. Remember: with power comes responsibility.</p>\n   <p class="pdT">Launch server when ready.</p>\n   <div class="clear"/>\n   <a class="btn btn-primary mdT js-startserver">Start server</a>\n ':user_accessible?user_accessible&&(__p+='\n    <div class="pdT pdB"><strong>Server access</strong> (choose one)</div>\n    <div class="btn-group">\n        <a class="btn js-webshell '+(null==(__t=use_web?"active":"")?"":__t)+'">Webshell</a>\n        <a class="btn js-terminal '+(null==(__t=use_web?"":"active")?"":__t)+'">Terminal login</a>\n    </div>\n   <div "js-timeleft"></div>\n   <div class="pdT"><strong>Task description</strong></div>\n   <div class="pdT">'+(null==(__t=question.question)?"":__t)+"</div>\n   ",task_attempt.task_descriptions&&(__p+='\n    <div class="pdT"><p>You may attempt the tasks in any order.<p></div>\n    <div class="pdT pdB"><strong>Tasks ('+(null==(__t=task_attempt.task_descriptions.length)?"":__t)+")</strong></div>\n   "),__p+="\n   <ul>\n   ",task_attempt.task_descriptions&&_.each(task_attempt.task_descriptions,function(t){__p+='\n     <li class="mdL">'+(null==(__t=t)?"":__t)+"</li>\n    "}),__p+='\n   </ul>\n   <a class="btn mdT backbone" href="'+(null==(__t=HR.candidate.candidateTestModel.get("unique_id"))?"":__t)+'/questions">Click here when done</a>\n '):(__p+=finished?'\n    <p class="pdT pdB"><strong>Task time completed.</strong><br/></p>\n    <p>Server is no longer accessible</p>\n    <a class="btn mdT backbone" href="'+(null==(__t=HR.candidate.candidateTestModel.get("unique_id"))?"":__t)+'/questions">Click here to close the test</a>\n    ':'\n   <p class="pdT">STATUS: <img src="//hrcdn.net/hackerrank/assets/ajax-msg-loader-4d8e554413e48d07592e67c5d804a2c1.gif"/> '+(null==(__t=server_state)?"":__t)+'</p>\n   <p class="pdT"><strong>Accessing server</strong><br/><small>(can take a moment)</small></p>\n   <div class="clear"/>\n   <a class="btn mdT js-refreshserver">Refresh</a>\n   <p class="pdT"><small>(Will auto refresh when ready)</small></p>\n   ',__p+="\n "),__p+='\n</div>\n<div class="span-xs-16 span-md-12 js-content-holder">\n ',user_accessible&&(__p+="\n  ",use_web?(url=task_attempt.proxy_url||"//"+task_attempt.ip_address+":81",__p+='\n    <div class="span-xs-16 span-md-8">\n      <strong>Username:</strong> '+(null==(__t=task_attempt.username)?"":__t)+", <strong>Password:</strong> "+(null==(__t=task_attempt.password)?"":__t)+'\n      <br/><a class="btn-link js-webshell-help"><i class="icon-keyboard"></i> Webshell help</a>\n    </div>\n    <div class="span-xs-16 span-md-8">\n      If the webshell interface seems slow, <a target="_blank" href="//'+(null==(__t=task_attempt.ip_address)?"":__t)+":81/?u="+(null==(__t=task_attempt.username)?"":__t)+"&p="+(null==(__t=task_attempt.password)?"":__t)+'">open in new tab</a>, or use terminal login.\n    </div>\n      <iframe src="'+(null==(__t=url)?"":__t)+"?u="+(null==(__t=task_attempt.username)?"":__t)+"&p="+(null==(__t=task_attempt.password)?"":__t)+'" width="100%" height="600px"></iframe>\n  '):__p+='\n    <div class="mdA">\n        <h4>Login details</h4>\n        <p class="pdT pdB">In your terminal or ssh app, use the following details to login</p>\n        <p><strong>IP address:</strong> '+(null==(__t=task_attempt.ip_address)?"":__t)+"</p>\n        <p><strong>User:</strong> "+(null==(__t=task_attempt.username)?"":__t)+"</p>\n        <p><strong>Password:</strong> "+(null==(__t=task_attempt.password)?"":__t)+"</p>\n    </div>\n  ",__p+="\n "),__p+="\n</div>\n";return __p});