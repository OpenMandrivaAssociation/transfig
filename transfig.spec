%define name	transfig
%define version	3.2.5d
%define release	%mkrel 4

Summary: A utility for converting FIG files (created by xfig) to other formats
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: 	 Graphics
Source: http://www.xfig.org/software/xfig/%{version}/%{name}.%{version}.tar.gz
Patch1: transfig.3.2.5-lib64support.patch
Patch2: transfig.3.2.5-use-tempfile-for-bitmap-eps.patch
Patch3: transfig.3.2.5-fix-str-fmt.patch
Patch4: transfig_optopt.patch
Patch5:	transfig.3.2.5-png1.5.patch
URL: http://www.xfig.org
Buildroot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libxpm-devel
BuildRequires: png-devel
BuildRequires: imake
BuildRequires: tcsh

%description
The transfig utility creates a makefile which translates FIG (created by xfig)
or PIC figures into a specified LaTeX graphics language (for example,
PostScript(TM)). Transfig is used to create TeX documents which are portable
(i.e., they can be printed in a wide variety of environments).

%prep
%setup -q -n %{name}.%{version}
%patch1 -p1 -b .lib64support
%patch2 -p1 -b .tmpepsfile
%patch3 -p0 -b .str
%patch4 -p1 -b .opt
%patch5 -p1

%build
xmkmf
make Makefiles

%ifarch alpha
%make EXTRA_DEFINES="-Dcfree=free"
%else
%make CDEBUGFLAGS="%optflags" SHLIBGLOBALSFLAGS="%ldflags" EXTRA_LDOPTIONS="%ldflags"
%endif

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install.man

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES NOTES README
%{_bindir}/*
%{_mandir}/man?/*
%{_prefix}/lib/X11/xfig/bitmaps
%{_datadir}/fig2dev/*.ps
