//  gcc test.c -I/usr/include/tk -ltk -ltcl
// 
#include <tk.h>
 
int main(int argc, char* argv[])
{
  Tcl_Interp* interp = Tcl_CreateInterp();
 
  Tcl_FindExecutable(argv[0]);
  Tcl_Init(interp);
  Tk_Init(interp);
 
  // char script[] = "pack [label .l -text {Hello, World!}]";
  // Tcl_Eval(interp, script);
  char script1[] = "label .l -text {123, 456}"; char script2[] = "lablel .l2  - text {Hello,  World!";
  Tcl_Eval(interp, script1);
  Tcl_Eval(interp, script2);
  char script3[] = "pack .l1 .l2"; 
  Tcl_Eval(interp, script3);
  Tk_MainLoop();
 
  Tcl_Finalize();
}
