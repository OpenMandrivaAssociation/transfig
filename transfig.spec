%define name	transfig
%define version	3.2.5
%define release	%mkrel 4
%if %{mdkversion} >= 200700
%define prefix	%{_prefix}
%define bindir	%{_bindir}
%define mandir	%{_mandir}
%else
%define prefix	/usr/X11R6
%define bindir	%{prefix}/bin
%define mandir	%{prefix}/man
%endif

Summary: A utility for converting FIG files (created by xfig) to other formats
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: 	 Graphics
Source: http://www.xfig.org/software/xfig/%{version}/%{name}.%{version}.tar.bz2
Patch1: transfig.3.2.5-lib64support.patch
Patch2: transfig.3.2.5-use-tempfile-for-bitmap-eps.patch
Patch3: transfig.3.2.5-fix-str-fmt.patch
URL: http://www.xfig.org
Buildroot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libjpeg-devel, libpng-devel, X11-devel, imake

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

%build
xmkmf
make Makefiles

%ifarch alpha
%make EXTRA_DEFINES="-Dcfree=free"
%else
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"
%endif

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES NOTES README
%{bindir}/fig2dev
%{bindir}/fig2ps2tex
%{bindir}/fig2ps2tex.sh
%{bindir}/pic2tpic
%{bindir}/transfig
%{mandir}/man?/*
%{prefix}/lib/X11/xfig/bitmaps
%dir %{_datadir}/fig2dev/
%{_datadir}/fig2dev/*.ps
