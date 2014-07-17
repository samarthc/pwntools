MAP_32BIT = 0x40
INADDR_ANY = 0
INADDR_BROADCAST = 0xffffffff
INADDR_NONE = 0xffffffff
INADDR_LOOPBACK = 0x7f000001
EPERM = 1
ENOENT = 2
ESRCH = 3
EINTR = 4
EIO = 5
ENXIO = 6
E2BIG = 7
ENOEXEC = 8
EBADF = 9
ECHILD = 10
EAGAIN = 11
ENOMEM = 12
EACCES = 13
EFAULT = 14
ENOTBLK = 15
EBUSY = 16
EEXIST = 17
EXDEV = 18
ENODEV = 19
ENOTDIR = 20
EISDIR = 21
EINVAL = 22
ENFILE = 23
EMFILE = 24
ENOTTY = 25
ETXTBSY = 26
EFBIG = 27
ENOSPC = 28
ESPIPE = 29
EROFS = 30
EMLINK = 31
EPIPE = 32
EDOM = 33
ERANGE = 34
ENOMSG = 35
EIDRM = 36
ECHRNG = 37
EL2NSYNC = 38
EL3HLT = 39
EL3RST = 40
ELNRNG = 41
EUNATCH = 42
ENOCSI = 43
EL2HLT = 44
EDEADLK = 45
ENOLCK = 46
EBADE = 50
EBADR = 51
EXFULL = 52
ENOANO = 53
EBADRQC = 54
EBADSLT = 55
EDEADLOCK = 56
EBFONT = 59
ENOSTR = 60
ENODATA = 61
ETIME = 62
ENOSR = 63
ENONET = 64
ENOPKG = 65
EREMOTE = 66
ENOLINK = 67
EADV = 68
ESRMNT = 69
ECOMM = 70
EPROTO = 71
EDOTDOT = 73
EMULTIHOP = 74
EBADMSG = 77
ENAMETOOLONG = 78
EOVERFLOW = 79
ENOTUNIQ = 80
EBADFD = 81
EREMCHG = 82
ELIBACC = 83
ELIBBAD = 84
ELIBSCN = 85
ELIBMAX = 86
ELIBEXEC = 87
EILSEQ = 88
ENOSYS = 89
ELOOP = 90
ERESTART = 91
ESTRPIPE = 92
ENOTEMPTY = 93
EUSERS = 94
ENOTSOCK = 95
EDESTADDRREQ = 96
EMSGSIZE = 97
EPROTOTYPE = 98
ENOPROTOOPT = 99
EPROTONOSUPPORT = 120
ESOCKTNOSUPPORT = 121
EOPNOTSUPP = 122
ENOTSUP = 122
EPFNOSUPPORT = 123
EAFNOSUPPORT = 124
EADDRINUSE = 125
EADDRNOTAVAIL = 126
ENETDOWN = 127
ENETUNREACH = 128
ENETRESET = 129
ECONNABORTED = 130
ECONNRESET = 131
ENOBUFS = 132
EISCONN = 133
ENOTCONN = 134
EUCLEAN = 135
ENOTNAM = 137
ENAVAIL = 138
EISNAM = 139
EREMOTEIO = 140
EINIT = 141
EREMDEV = 142
ESHUTDOWN = 143
ETOOMANYREFS = 144
ETIMEDOUT = 145
ECONNREFUSED = 146
EHOSTDOWN = 147
EHOSTUNREACH = 148
EWOULDBLOCK = 11
EALREADY = 149
EINPROGRESS = 150
ESTALE = 151
ECANCELED = 158
ENOMEDIUM = 159
EMEDIUMTYPE = 160
ENOKEY = 161
EKEYEXPIRED = 162
EKEYREVOKED = 163
EKEYREJECTED = 164
EDQUOT = 1133
__SYS_NERR = ((164) + 1)
__LITTLE_ENDIAN = 1234
__BIG_ENDIAN = 4321
__BYTE_ORDER = 1234
__FLOAT_WORD_ORDER = 1234
LITTLE_ENDIAN = 1234
BIG_ENDIAN = 4321
BYTE_ORDER = 1234
__WORDSIZE = 64
__FSUID_H = 1
NSIG = 32
_NSIG = 128
SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGABRT = 6
SIGIOT = 6
SIGFPE = 8
SIGKILL = 9
SIGSEGV = 11
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGUNUSED = 31
SIGEMT = 7
SIGBUS = 10
SIGSYS = 12
SIGUSR1 = 16
SIGUSR2 = 17
SIGCHLD = 18
SIGPWR = 19
SIGWINCH = 20
SIGURG = 21
SIGIO = 22
SIGSTOP = 23
SIGTSTP = 24
SIGCONT = 25
SIGTTIN = 26
SIGTTOU = 27
SIGVTALRM = 28
SIGPROF = 29
SIGXCPU = 30
SIGXFSZ = 31
SIGCLD = 18
SIGPOLL = 22
SIGLOST = 19
SIGRTMIN = 32
SIGRTMAX = (128-1)
SA_NOCLDSTOP = 0x00000001
SA_SIGINFO = 0x00000008
SA_NOCLDWAIT = 0x00010000
SA_RESTORER = 0x04000000
SA_ONSTACK = 0x08000000
SA_RESTART = 0x10000000
SA_INTERRUPT = 0x20000000
SA_NODEFER = 0x40000000
SA_RESETHAND = 0x80000000
SA_NOMASK = 0x40000000
SA_ONESHOT = 0x80000000
SS_ONSTACK = 1
SS_DISABLE = 2
MINSIGSTKSZ = 2048
SIGSTKSZ = 8192
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SI_MAX_SIZE = 128
SIGEV_SIGNAL = 0
SIGEV_NONE = 1
SIGEV_THREAD = 2
SIGEV_THREAD_ID = 4
SIGEV_MAX_SIZE = 64
_SYS_TIME_H = 1
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
FD_SETSIZE = 1024
R_OK = 4
W_OK = 2
X_OK = 1
F_OK = 0
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2
STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2
_CS_PATH = 1
_SC_CLK_TCK = 1
_SC_ARG_MAX = 2
_SC_NGROUPS_MAX = 3
_SC_OPEN_MAX = 4
_SC_PAGESIZE = 5
_SC_NPROCESSORS_ONLN = 6
_SC_NPROCESSORS_CONF = 6
_SC_PHYS_PAGES = 7
_PC_PATH_MAX = 1
_PC_VDISABLE = 2
L_cuserid = 17
_POSIX_VERSION = 199506
F_ULOCK = 0
F_LOCK = 1
F_TLOCK = 2
F_TEST = 3
S_IFMT = 00170000
S_IFSOCK = 0140000
S_IFLNK = 0120000
S_IFREG = 0100000
S_IFBLK = 0060000
S_IFDIR = 0040000
S_IFCHR = 0020000
S_IFIFO = 0010000
S_ISUID = 0004000
S_ISGID = 0002000
S_ISVTX = 0001000
S_IRWXU = 00700
S_IRUSR = 00400
S_IWUSR = 00200
S_IXUSR = 00100
S_IRWXG = 00070
S_IRGRP = 00040
S_IWGRP = 00020
S_IXGRP = 00010
S_IRWXO = 00007
S_IROTH = 00004
S_IWOTH = 00002
S_IXOTH = 00001
S_IREAD = 00400
S_IWRITE = 00200
S_IEXEC = 00100
F_LINUX_SPECIFIC_BASE = 1024
O_ACCMODE = 0x0003
O_RDONLY = 0x0000
O_WRONLY = 0x0001
O_RDWR = 0x0002
O_APPEND = 0x0008
O_SYNC = 0x0010
O_NONBLOCK = 0x0080
O_CREAT = 0x0100
O_TRUNC = 0x0200
O_EXCL = 0x0400
O_NOCTTY = 0x0800
FASYNC = 0x1000
O_LARGEFILE = 0x2000
O_DIRECT = 0x8000
O_DIRECTORY = 0x10000
O_NOFOLLOW = 0x20000
O_NOATIME = 0x40000
O_NDELAY = 0x0080
F_DUPFD = 0
F_GETFD = 1
F_SETFD = 2
F_GETFL = 3
F_SETFL = 4
F_GETLK = 14
F_SETLK = 6
F_SETLKW = 7
F_SETOWN = 24
F_GETOWN = 23
F_SETSIG = 10
F_GETSIG = 11
FD_CLOEXEC = 1
F_RDLCK = 0
F_WRLCK = 1
F_UNLCK = 2
F_EXLCK = 4
F_SHLCK = 8
F_INPROGRESS = 16
LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8
LOCK_MAND = 32
LOCK_READ = 64
LOCK_WRITE = 128
LOCK_RW = 192
O_ASYNC = 0x1000
MREMAP_MAYMOVE = 1
MREMAP_FIXED = 2
PROT_READ = 0x1
PROT_WRITE = 0x2
PROT_EXEC = 0x4
PROT_NONE = 0x0
MAP_SHARED = 0x01
MAP_PRIVATE = 0x02
MAP_FIXED = 0x010
MAP_NORESERVE = 0x0400
MAP_ANONYMOUS = 0x0800
MAP_GROWSDOWN = 0x1000
MAP_DENYWRITE = 0x2000
MAP_EXECUTABLE = 0x4000
MAP_LOCKED = 0x8000
MAP_POPULATE = 0x10000
MS_ASYNC = 0x0001
MS_INVALIDATE = 0x0002
MS_SYNC = 0x0004
MCL_CURRENT = 1
MCL_FUTURE = 2
MADV_NORMAL = 0x0
MADV_RANDOM = 0x1
MADV_SEQUENTIAL = 0x2
MADV_WILLNEED = 0x3
MADV_DONTNEED = 0x4
MAP_ANON = 0x0800
MAP_FILE = 0
SOL_SOCKET = 0xffff
SO_DEBUG = 0x0001
SO_REUSEADDR = 0x0004
SO_TYPE = 0x1008
SO_ERROR = 0x1007
SO_DONTROUTE = 0x0010
SO_BROADCAST = 0x0020
SO_SNDBUF = 0x1001
SO_RCVBUF = 0x1002
SO_KEEPALIVE = 0x0008
SO_OOBINLINE = 0x0100
SO_NO_CHECK = 11
SO_PRIORITY = 12
SO_LINGER = 0x0080
SO_BSDCOMPAT = 14
SO_PASSCRED = 17
SO_PEERCRED = 18
SO_RCVLOWAT = 0x1004
SO_SNDLOWAT = 0x1003
SO_RCVTIMEO = 0x1006
SO_SNDTIMEO = 0x1005
SO_ACCEPTCONN = 0x1009
SO_SNDBUFFORCE = 31
SO_RCVBUFFORCE = 33
SO_STYLE = 0x1008
SO_SECURITY_AUTHENTICATION = 22
SO_SECURITY_ENCRYPTION_TRANSPORT = 23
SO_SECURITY_ENCRYPTION_NETWORK = 24
SO_BINDTODEVICE = 25
SO_ATTACH_FILTER = 26
SO_DETACH_FILTER = 27
SO_PEERNAME = 28
SO_TIMESTAMP = 29
SCM_TIMESTAMP = 29
SOCK_DGRAM = 1
SOCK_STREAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_PACKET = 10
UIO_FASTIOV = 8
UIO_MAXIOV = 1024
SCM_RIGHTS = 0x01
SCM_CREDENTIALS = 0x02
SCM_CONNECT = 0x03
AF_UNSPEC = 0
AF_UNIX = 1
AF_LOCAL = 1
AF_INET = 2
AF_AX25 = 3
AF_IPX = 4
AF_APPLETALK = 5
AF_NETROM = 6
AF_BRIDGE = 7
AF_ATMPVC = 8
AF_X25 = 9
AF_INET6 = 10
AF_ROSE = 11
AF_DECnet = 12
AF_NETBEUI = 13
AF_SECURITY = 14
AF_KEY = 15
AF_NETLINK = 16
AF_ROUTE = 16
AF_PACKET = 17
AF_ASH = 18
AF_ECONET = 19
AF_ATMSVC = 20
AF_SNA = 22
AF_IRDA = 23
AF_PPPOX = 24
AF_WANPIPE = 25
AF_MAX = 32
PF_UNSPEC = 0
PF_UNIX = 1
PF_LOCAL = 1
PF_INET = 2
PF_AX25 = 3
PF_IPX = 4
PF_APPLETALK = 5
PF_NETROM = 6
PF_BRIDGE = 7
PF_ATMPVC = 8
PF_X25 = 9
PF_INET6 = 10
PF_ROSE = 11
PF_DECnet = 12
PF_NETBEUI = 13
PF_SECURITY = 14
PF_KEY = 15
PF_NETLINK = 16
PF_ROUTE = 16
PF_PACKET = 17
PF_ASH = 18
PF_ECONET = 19
PF_ATMSVC = 20
PF_SNA = 22
PF_IRDA = 23
PF_PPPOX = 24
PF_WANPIPE = 25
PF_MAX = 32
SOMAXCONN = 128
MSG_OOB = 1
MSG_PEEK = 2
MSG_DONTROUTE = 4
MSG_TRYHARD = 4
MSG_CTRUNC = 8
MSG_PROBE = 0x10
MSG_TRUNC = 0x20
MSG_DONTWAIT = 0x40
MSG_EOR = 0x80
MSG_WAITALL = 0x100
MSG_FIN = 0x200
MSG_EOF = 0x200
MSG_SYN = 0x400
MSG_CONFIRM = 0x800
MSG_RST = 0x1000
MSG_ERRQUEUE = 0x2000
MSG_NOSIGNAL = 0x4000
MSG_MORE = 0x8000
SOL_IP = 0
SOL_TCP = 6
SOL_UDP = 17
SOL_IPV6 = 41
SOL_ICMPV6 = 58
SOL_RAW = 255
SOL_IPX = 256
SOL_AX25 = 257
SOL_ATALK = 258
SOL_NETROM = 259
SOL_ROSE = 260
SOL_DECNET = 261
SOL_X25 = 262
SOL_PACKET = 263
SOL_ATM = 264
SOL_AAL = 265
SOL_IRDA = 266
IPX_TYPE = 1
SHUT_RD = 0
SHUT_WR = 1
SHUT_RDWR = 2
NI_NOFQDN = 1
NI_NUMERICHOST = 2
NI_NAMEREQD = 4
NI_NUMERICSERV = 8
NI_DGRAM = 16
EAI_FAMILY = -1
EAI_SOCKTYPE = -2
EAI_BADFLAGS = -3
EAI_NONAME = -4
EAI_SERVICE = -5
EAI_ADDRFAMILY = -6
EAI_NODATA = -7
EAI_MEMORY = -8
EAI_FAIL = -9
EAI_AGAIN = -10
EAI_SYSTEM = -11
AI_NUMERICHOST = 1
AI_CANONNAME = 2
AI_PASSIVE = 4
SIOCADDRT = 0x890B
SIOCDELRT = 0x890C
SIOCRTMSG = 0x890D
SIOCGIFNAME = 0x8910
SIOCSIFLINK = 0x8911
SIOCGIFCONF = 0x8912
SIOCGIFFLAGS = 0x8913
SIOCSIFFLAGS = 0x8914
SIOCGIFADDR = 0x8915
SIOCSIFADDR = 0x8916
SIOCGIFDSTADDR = 0x8917
SIOCSIFDSTADDR = 0x8918
SIOCGIFBRDADDR = 0x8919
SIOCSIFBRDADDR = 0x891a
SIOCGIFNETMASK = 0x891b
SIOCSIFNETMASK = 0x891c
SIOCGIFMETRIC = 0x891d
SIOCSIFMETRIC = 0x891e
SIOCGIFMEM = 0x891f
SIOCSIFMEM = 0x8920
SIOCGIFMTU = 0x8921
SIOCSIFMTU = 0x8922
SIOCSIFNAME = 0x8923
SIOCSIFHWADDR = 0x8924
SIOCGIFENCAP = 0x8925
SIOCSIFENCAP = 0x8926
SIOCGIFHWADDR = 0x8927
SIOCGIFSLAVE = 0x8929
SIOCSIFSLAVE = 0x8930
SIOCADDMULTI = 0x8931
SIOCDELMULTI = 0x8932
SIOCGIFINDEX = 0x8933
SIOGIFINDEX = 0x8933
SIOCSIFPFLAGS = 0x8934
SIOCGIFPFLAGS = 0x8935
SIOCDIFADDR = 0x8936
SIOCSIFHWBROADCAST = 0x8937
SIOCGIFCOUNT = 0x8938
SIOCGIFBR = 0x8940
SIOCSIFBR = 0x8941
SIOCGIFTXQLEN = 0x8942
SIOCSIFTXQLEN = 0x8943
SIOCGIFDIVERT = 0x8944
SIOCSIFDIVERT = 0x8945
SIOCETHTOOL = 0x8946
SIOCDARP = 0x8953
SIOCGARP = 0x8954
SIOCSARP = 0x8955
SIOCDRARP = 0x8960
SIOCGRARP = 0x8961
SIOCSRARP = 0x8962
SIOCGIFMAP = 0x8970
SIOCSIFMAP = 0x8971
SIOCADDDLCI = 0x8980
SIOCDELDLCI = 0x8981
SIOCDEVPRIVATE = 0x89F0
PTRACE_TRACEME = 0
PTRACE_PEEKTEXT = 1
PTRACE_PEEKDATA = 2
PTRACE_PEEKUSR = 3
PTRACE_PEEKUSER = 3
PTRACE_POKETEXT = 4
PTRACE_POKEDATA = 5
PTRACE_POKEUSR = 6
PTRACE_POKEUSER = 6
PTRACE_CONT = 7
PTRACE_KILL = 8
PTRACE_SINGLESTEP = 9
PTRACE_ATTACH = 0x10
PTRACE_DETACH = 0x11
PTRACE_SYSCALL = 24
PTRACE_GETEVENTMSG = 0x4201
PTRACE_GETSIGINFO = 0x4202
PTRACE_SETSIGINFO = 0x4203
PTRACE_O_TRACESYSGOOD = 0x00000001
PTRACE_O_TRACEFORK = 0x00000002
PTRACE_O_TRACEVFORK = 0x00000004
PTRACE_O_TRACECLONE = 0x00000008
PTRACE_O_TRACEEXEC = 0x00000010
PTRACE_O_TRACEVFORKDONE = 0x00000020
PTRACE_O_TRACEEXIT = 0x00000040
PTRACE_O_MASK = 0x0000007f
PTRACE_EVENT_FORK = 1
PTRACE_EVENT_VFORK = 2
PTRACE_EVENT_CLONE = 3
PTRACE_EVENT_EXEC = 4
PTRACE_EVENT_VFORK_DONE = 5
PTRACE_EVENT_EXIT = 6
PT_TRACE_ME = 0
PT_READ_I = 1
PT_READ_D = 2
PT_READ_U = 3
PT_WRITE_I = 4
PT_WRITE_D = 5
PT_WRITE_U = 6
PT_CONTINUE = 7
PT_KILL = 8
PT_STEP = 9
PT_ATTACH = 0x10
PT_DETACH = 0x11
FPR_BASE = 32
PC = 64
CAUSE = 65
BADVADDR = 66
MMHI = 67
MMLO = 68
FPC_CSR = 69
FPC_EIR = 70
__NR_Linux = 4000
__NR_syscall = (4000 +   0)
__NR_exit = (4000 +   1)
__NR_fork = (4000 +   2)
__NR_read = (4000 +   3)
__NR_write = (4000 +   4)
__NR_open = (4000 +   5)
__NR_close = (4000 +   6)
__NR_waitpid = (4000 +   7)
__NR_creat = (4000 +   8)
__NR_link = (4000 +   9)
__NR_unlink = (4000 +  10)
__NR_execve = (4000 +  11)
__NR_chdir = (4000 +  12)
__NR_time = (4000 +  13)
__NR_mknod = (4000 +  14)
__NR_chmod = (4000 +  15)
__NR_lchown = (4000 +  16)
__NR_break = (4000 +  17)
__NR_unused18 = (4000 +  18)
__NR_lseek = (4000 +  19)
__NR_getpid = (4000 +  20)
__NR_mount = (4000 +  21)
__NR_umount = (4000 +  22)
__NR_setuid = (4000 +  23)
__NR_getuid = (4000 +  24)
__NR_stime = (4000 +  25)
__NR_ptrace = (4000 +  26)
__NR_alarm = (4000 +  27)
__NR_unused28 = (4000 +  28)
__NR_pause = (4000 +  29)
__NR_utime = (4000 +  30)
__NR_stty = (4000 +  31)
__NR_gtty = (4000 +  32)
__NR_access = (4000 +  33)
__NR_nice = (4000 +  34)
__NR_ftime = (4000 +  35)
__NR_sync = (4000 +  36)
__NR_kill = (4000 +  37)
__NR_rename = (4000 +  38)
__NR_mkdir = (4000 +  39)
__NR_rmdir = (4000 +  40)
__NR_dup = (4000 +  41)
__NR_pipe = (4000 +  42)
__NR_times = (4000 +  43)
__NR_prof = (4000 +  44)
__NR_brk = (4000 +  45)
__NR_setgid = (4000 +  46)
__NR_getgid = (4000 +  47)
__NR_signal = (4000 +  48)
__NR_geteuid = (4000 +  49)
__NR_getegid = (4000 +  50)
__NR_acct = (4000 +  51)
__NR_umount2 = (4000 +  52)
__NR_lock = (4000 +  53)
__NR_ioctl = (4000 +  54)
__NR_fcntl = (4000 +  55)
__NR_mpx = (4000 +  56)
__NR_setpgid = (4000 +  57)
__NR_ulimit = (4000 +  58)
__NR_unused59 = (4000 +  59)
__NR_umask = (4000 +  60)
__NR_chroot = (4000 +  61)
__NR_ustat = (4000 +  62)
__NR_dup2 = (4000 +  63)
__NR_getppid = (4000 +  64)
__NR_getpgrp = (4000 +  65)
__NR_setsid = (4000 +  66)
__NR_sigaction = (4000 +  67)
__NR_sgetmask = (4000 +  68)
__NR_ssetmask = (4000 +  69)
__NR_setreuid = (4000 +  70)
__NR_setregid = (4000 +  71)
__NR_sigsuspend = (4000 +  72)
__NR_sigpending = (4000 +  73)
__NR_sethostname = (4000 +  74)
__NR_setrlimit = (4000 +  75)
__NR_getrlimit = (4000 +  76)
__NR_getrusage = (4000 +  77)
__NR_gettimeofday = (4000 +  78)
__NR_settimeofday = (4000 +  79)
__NR_getgroups = (4000 +  80)
__NR_setgroups = (4000 +  81)
__NR_reserved82 = (4000 +  82)
__NR_symlink = (4000 +  83)
__NR_unused84 = (4000 +  84)
__NR_readlink = (4000 +  85)
__NR_uselib = (4000 +  86)
__NR_swapon = (4000 +  87)
__NR_reboot = (4000 +  88)
__NR_readdir = (4000 +  89)
__NR_mmap = (4000 +  90)
__NR_munmap = (4000 +  91)
__NR_truncate = (4000 +  92)
__NR_ftruncate = (4000 +  93)
__NR_fchmod = (4000 +  94)
__NR_fchown = (4000 +  95)
__NR_getpriority = (4000 +  96)
__NR_setpriority = (4000 +  97)
__NR_profil = (4000 +  98)
__NR_statfs = (4000 +  99)
__NR_fstatfs = (4000 + 100)
__NR_ioperm = (4000 + 101)
__NR_socketcall = (4000 + 102)
__NR_syslog = (4000 + 103)
__NR_setitimer = (4000 + 104)
__NR_getitimer = (4000 + 105)
__NR_stat = (4000 + 106)
__NR_lstat = (4000 + 107)
__NR_fstat = (4000 + 108)
__NR_unused109 = (4000 + 109)
__NR_iopl = (4000 + 110)
__NR_vhangup = (4000 + 111)
__NR_idle = (4000 + 112)
__NR_vm86 = (4000 + 113)
__NR_wait4 = (4000 + 114)
__NR_swapoff = (4000 + 115)
__NR_sysinfo = (4000 + 116)
__NR_ipc = (4000 + 117)
__NR_fsync = (4000 + 118)
__NR_sigreturn = (4000 + 119)
__NR_clone = (4000 + 120)
__NR_setdomainname = (4000 + 121)
__NR_uname = (4000 + 122)
__NR_modify_ldt = (4000 + 123)
__NR_adjtimex = (4000 + 124)
__NR_mprotect = (4000 + 125)
__NR_sigprocmask = (4000 + 126)
__NR_create_module = (4000 + 127)
__NR_init_module = (4000 + 128)
__NR_delete_module = (4000 + 129)
__NR_get_kernel_syms = (4000 + 130)
__NR_quotactl = (4000 + 131)
__NR_getpgid = (4000 + 132)
__NR_fchdir = (4000 + 133)
__NR_bdflush = (4000 + 134)
__NR_sysfs = (4000 + 135)
__NR_personality = (4000 + 136)
__NR_afs_syscall = (4000 + 137)
__NR_setfsuid = (4000 + 138)
__NR_setfsgid = (4000 + 139)
__NR__llseek = (4000 + 140)
__NR_getdents = (4000 + 141)
__NR__newselect = (4000 + 142)
__NR_flock = (4000 + 143)
__NR_msync = (4000 + 144)
__NR_readv = (4000 + 145)
__NR_writev = (4000 + 146)
__NR_cacheflush = (4000 + 147)
__NR_cachectl = (4000 + 148)
__NR_sysmips = (4000 + 149)
__NR_unused150 = (4000 + 150)
__NR_getsid = (4000 + 151)
__NR_fdatasync = (4000 + 152)
__NR__sysctl = (4000 + 153)
__NR_mlock = (4000 + 154)
__NR_munlock = (4000 + 155)
__NR_mlockall = (4000 + 156)
__NR_munlockall = (4000 + 157)
__NR_sched_setparam = (4000 + 158)
__NR_sched_getparam = (4000 + 159)
__NR_sched_setscheduler = (4000 + 160)
__NR_sched_getscheduler = (4000 + 161)
__NR_sched_yield = (4000 + 162)
__NR_sched_get_priority_max = (4000 + 163)
__NR_sched_get_priority_min = (4000 + 164)
__NR_sched_rr_get_interval = (4000 + 165)
__NR_nanosleep = (4000 + 166)
__NR_mremap = (4000 + 167)
__NR_accept = (4000 + 168)
__NR_bind = (4000 + 169)
__NR_connect = (4000 + 170)
__NR_getpeername = (4000 + 171)
__NR_getsockname = (4000 + 172)
__NR_getsockopt = (4000 + 173)
__NR_listen = (4000 + 174)
__NR_recv = (4000 + 175)
__NR_recvfrom = (4000 + 176)
__NR_recvmsg = (4000 + 177)
__NR_send = (4000 + 178)
__NR_sendmsg = (4000 + 179)
__NR_sendto = (4000 + 180)
__NR_setsockopt = (4000 + 181)
__NR_shutdown = (4000 + 182)
__NR_socket = (4000 + 183)
__NR_socketpair = (4000 + 184)
__NR_setresuid = (4000 + 185)
__NR_getresuid = (4000 + 186)
__NR_query_module = (4000 + 187)
__NR_poll = (4000 + 188)
__NR_nfsservctl = (4000 + 189)
__NR_setresgid = (4000 + 190)
__NR_getresgid = (4000 + 191)
__NR_prctl = (4000 + 192)
__NR_rt_sigreturn = (4000 + 193)
__NR_rt_sigaction = (4000 + 194)
__NR_rt_sigprocmask = (4000 + 195)
__NR_rt_sigpending = (4000 + 196)
__NR_rt_sigtimedwait = (4000 + 197)
__NR_rt_sigqueueinfo = (4000 + 198)
__NR_rt_sigsuspend = (4000 + 199)
__NR_pread = (4000 + 200)
__NR_pwrite = (4000 + 201)
__NR_chown = (4000 + 202)
__NR_getcwd = (4000 + 203)
__NR_capget = (4000 + 204)
__NR_capset = (4000 + 205)
__NR_sigaltstack = (4000 + 206)
__NR_sendfile = (4000 + 207)
__NR_getpmsg = (4000 + 208)
__NR_putpmsg = (4000 + 209)
__NR_mmap2 = (4000 + 210)
__NR_truncate64 = (4000 + 211)
__NR_ftruncate64 = (4000 + 212)
__NR_stat64 = (4000 + 213)
__NR_lstat64 = (4000 + 214)
__NR_fstat64 = (4000 + 215)
__NR_pivot_root = (4000 + 216)
__NR_mincore = (4000 + 217)
__NR_madvise = (4000 + 218)
__NR_getdents64 = (4000 + 219)
__NR_fcntl64 = (4000 + 220)
__NR_reserved221 = (4000 + 221)
__NR_gettid = (4000 + 222)
__NR_readahead = (4000 + 223)
__NR_setxattr = (4000 + 224)
__NR_lsetxattr = (4000 + 225)
__NR_fsetxattr = (4000 + 226)
__NR_getxattr = (4000 + 227)
__NR_lgetxattr = (4000 + 228)
__NR_fgetxattr = (4000 + 229)
__NR_listxattr = (4000 + 230)
__NR_llistxattr = (4000 + 231)
__NR_flistxattr = (4000 + 232)
__NR_removexattr = (4000 + 233)
__NR_lremovexattr = (4000 + 234)
__NR_fremovexattr = (4000 + 235)
__NR_tkill = (4000 + 236)
__NR_sendfile64 = (4000 + 237)
__NR_futex = (4000 + 238)
__NR_sched_setaffinity = (4000 + 239)
__NR_sched_getaffinity = (4000 + 240)
__NR_io_setup = (4000 + 241)
__NR_io_destroy = (4000 + 242)
__NR_io_getevents = (4000 + 243)
__NR_io_submit = (4000 + 244)
__NR_io_cancel = (4000 + 245)
__NR_exit_group = (4000 + 246)
__NR_lookup_dcookie = (4000 + 247)
__NR_epoll_create = (4000 + 248)
__NR_epoll_ctl = (4000 + 249)
__NR_epoll_wait = (4000 + 250)
__NR_remap_file_pages = (4000 + 251)
__NR_set_tid_address = (4000 + 252)
__NR_restart_syscall = (4000 + 253)
__NR_fadvise64 = (4000 + 254)
__NR_statfs64 = (4000 + 255)
__NR_fstatfs64 = (4000 + 256)
__NR_timer_create = (4000 + 257)
__NR_timer_settime = (4000 + 258)
__NR_timer_gettime = (4000 + 259)
__NR_timer_getoverrun = (4000 + 260)
__NR_timer_delete = (4000 + 261)
__NR_clock_settime = (4000 + 262)
__NR_clock_gettime = (4000 + 263)
__NR_clock_getres = (4000 + 264)
__NR_clock_nanosleep = (4000 + 265)
__NR_tgkill = (4000 + 266)
__NR_utimes = (4000 + 267)
__NR_mbind = (4000 + 268)
__NR_get_mempolicy = (4000 + 269)
__NR_set_mempolicy = (4000 + 270)
__NR_mq_open = (4000 + 271)
__NR_mq_unlink = (4000 + 272)
__NR_mq_timedsend = (4000 + 273)
__NR_mq_timedreceive = (4000 + 274)
__NR_mq_notify = (4000 + 275)
__NR_mq_getsetattr = (4000 + 276)
__NR_vserver = (4000 + 277)
__NR_waitid = (4000 + 278)
__NR_add_key = (4000 + 280)
__NR_request_key = (4000 + 281)
__NR_keyctl = (4000 + 282)
__NR_set_thread_area = (4000 + 283)
__NR_inotify_init = (4000 + 284)
__NR_inotify_add_watch = (4000 + 285)
__NR_inotify_rm_watch = (4000 + 286)
__NR_migrate_pages = (4000 + 287)
__NR_openat = (4000 + 288)
__NR_mkdirat = (4000 + 289)
__NR_mknodat = (4000 + 290)
__NR_fchownat = (4000 + 291)
__NR_futimesat = (4000 + 292)
__NR_fstatat = (4000 + 293)
__NR_unlinkat = (4000 + 294)
__NR_renameat = (4000 + 295)
__NR_linkat = (4000 + 296)
__NR_symlinkat = (4000 + 297)
__NR_readlinkat = (4000 + 298)
__NR_fchmodat = (4000 + 299)
__NR_faccessat = (4000 + 300)
__NR_pselect6 = (4000 + 301)
__NR_ppoll = (4000 + 302)
__NR_unshare = (4000 + 303)
__NR_splice = (4000 + 304)
__NR_sync_file_range = (4000 + 305)
__NR_tee = (4000 + 306)
__NR_vmsplice = (4000 + 307)
__NR_move_pages = (4000 + 308)
__NR_set_robust_list = (4000 + 272)
__NR_get_robust_list = (4000 + 273)
__NR_kexec_load = (4000 + 274)
__NR_getcpu = (4000 + 275)
__NR_epoll_pwait = (4000 + 276)
__NR_ioprio_set = (4000 + 277)
__NR_ioprio_get = (4000 + 278)
__NR_utimensat = (4000 + 279)
__NR_signalfd = (4000 + 280)
__NR_timerfd = (4000 + 281)
__NR_eventfd = (4000 + 282)
__NR_fallocate = (4000 + 283)
__NR_timerfd_create = (4000 + 284)
__NR_timerfd_gettime = (4000 + 285)
__NR_timerfd_settime = (4000 + 286)