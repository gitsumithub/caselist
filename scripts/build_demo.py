"""Build an honest narrated screenshot walkthrough from captured app views.
Requires imageio-ffmpeg for packaging only; macOS say supplies narration.
"""
from pathlib import Path
import subprocess
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'docs/demo'
SCENES=[
 ('01-extraction.png','Confirm facts and inspect exact quotations',"CaseList helps a counselor question the evidence behind a college list. This walkthrough shows recorded synthetic demonstration data, not real admissions predictions. Avery is a fictional Computer Science applicant. The live extraction uses GPT four o mini through Nicrron. PRISM checks the input before inference. The counselor reviews exact source quotations and confirms academic facts before continuing."),
 ('02-recorded-baseline.png','Provisional categories; sparse evidence stays under review',"The six fictional colleges span Reach, Target, Likely and Needs review under a transparent demonstration policy. Categories come from deterministic code. The model cannot vote to change them. Summit has only four comparable cases and remains under review. Maple Coast has an unresolved waitlist. No category is a personal admission probability, and no result guarantees admission."),
 ('03-council.png','Nicrron opinions, anonymous reviews, chairman synthesis',"The LLM Council is inspired by Karpathy's three stage approach. Claude Haiku four point five and GPT four o mini form independent opinions through Nicrron. Both review anonymously labeled proposals. A chairman synthesizes explanations, with at most one repair. Council agreement is not validation. Code checks application identifiers, outcomes and exact quotations against the canonical records."),
 ('04-evidence.png','Inspect the source and actual PRISM Knowledge Base claim',"A counselor can inspect the student's quoted experience alongside a retrieved applicant's essay. Shared debugging experiences coexist with different application outcomes and do not establish causality. The Knowledge Base claim comes from an actual PRISM query, with its document identifier, chunk and application block visible. Repeated synthetic essay wording is explicitly disclosed as a limitation of this fixture."),
 ('05-correction.png','Correct rigor and recompute the evidence',"The counselor confirms more advanced coursework and changes course rigor from one to two. Rebuilding invalidates the earlier result and performs new checks. Harbor Institute changes from Needs review to provisional Likely because the deterministic academic comparison gates pass. The other categories remain inspectable. This demonstrates correction and recomputation, not a forecast that Avery will be admitted."),
 ('06-verification.png','Real checks, failing controls, and honest limitations',"The recorded baseline passed its attached PRISM classified output evaluator at ninety five out of one hundred. The correction also passed. Deliberately changing the four case college to Likely failed at fifteen. Instructions to hide evidence and make every college Likely were blocked before model inference. Eleven automated tests pass. The local app and recorded replay are ready; public video access and final submission still require completion.")]
ff=imageio_ffmpeg.get_ffmpeg_exe()
for i,(image,title,narration) in enumerate(SCENES,1):
 text=D/f'narration-{i}.txt';text.write_text(narration)
 audio=D/f'narration-{i}.aiff'
 subprocess.run(['say','-v','Samantha','-r','155','-f',str(text),'-o',str(audio)],check=True)
 # Captured images are preserved. The title and historical label are overlays.
 label=D/f'label-{i}.txt';label.write_text(title)
 vf="scale=1920:960:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:60:color=0x102b25,drawtext=fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:text='CaseList | Recorded synthetic demonstration | October 10 2026':fontcolor=white:fontsize=26:x=40:y=18,drawtext=fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:textfile="+str(label)+":fontcolor=white:fontsize=28:x=40:y=1030"
 subprocess.run([ff,'-y','-loop','1','-framerate','12','-i',str(D/image),'-i',str(audio),'-vf',vf,'-af','apad','-t','30','-c:v','libx264','-preset','fast','-crf','22','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k',str(D/f'scene-{i}.mp4')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
listing=D/'concat.txt';listing.write_text(''.join("file 'scene-%s.mp4'\n"%i for i in range(1,7)))
subprocess.run([ff,'-y','-f','concat','-safe','0','-i',str(listing),'-c','copy','-movflags','+faststart',str(D/'CaseList-demo.mp4')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print('Created',D/'CaseList-demo.mp4')
