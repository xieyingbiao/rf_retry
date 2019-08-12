# -*- coding: utf-8 -*-
import sys
args=sys.argv[1:]
logdir=''
i=0
for a in args:
    if (a=='-o'):
        logdir=args[i+1]
        break
    i=i+1
args[i+1]=logdir+'_first_run.xml'
log1dir=logdir+'_first_run.xml'
all_comm='''echo 第一次执行脚本
{0}
if [ $? -eq 0 ]; then
    {2}
    exit 0
else
    echo 第二次重试执行脚本
    {1}
    echo 生成新的日志
    {3}
fi
'''
file_object = open('./run_cli.sh', 'w')
comm1='pybot '+ ' '.join(str(i) for i in args)
args[i+1]=logdir+'_second_run.xml'
log2dir=logdir+'_second_run.xml'
args.remove(args[-1])
args.append('-R')
args.append(logdir+'_first_run.xml')
args.append('suites')
comm2='pybot '+ ' '.join(str(i) for i in args)
comm3='''rebot -d '''+logdir+''' -R --splitlog -x outputxunit.xml '''+log1dir+''''''
comm4='''rebot -d '''+logdir+''' -R --splitlog -o output.xml -x outputxunit.xml '''+log1dir+''' '''+log2dir+''''''
file_object.writelines(all_comm.format(comm1,comm2,comm3,comm4))
file_object.close()
#python retry_run.py -o log/$(BUILD.BUILDID) -i $(run_tag) -e NO -l None -r None -P lib suites
