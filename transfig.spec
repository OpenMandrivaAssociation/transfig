%define name	transfig
%define version	3.2.5
%define aversion alpha7
%define release	%mkrel 0.5
%if %{mdkversion} >= 200700
%define prefix	%{_prefix}
%define bindir	%{_bindir}
%define mandir	%{_mandir}
%else
%define prefix	/usr/X11R6
%define bindir	%{prefix}/bin
%define mandir	%{prefix}/man
%endif

Summary: A utility for converting FIG files (made by xfig) to other formats
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: Graphics
Source: ftp://ftp.x.org/contrib/applications/drawing_tools/transfig/%{name}.%{version}_%{aversion}.tar.bz2
Patch1: transfig-3.2.5-lib64support.patch
Patch2: transfig.3.2.3d-includes.patch
#Patch3: transfig.3.2.3d-strerror.patch
#Patch4: transfig.3.2.5-alpha5-gcc4.patch
Patch5: transfig.3.2.5-alpha5-dotsyms.patch
Patch6: transfig.3.2.5_alpha7-use-tempfile-for-bitmap-eps.patch
URL: http://www.xfig.org
Buildroot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libjpeg-devel, libpng-devel, X11-devel, imake

%description
The transfig utility creates a makefile which translates FIG (created by xfig)
or PIC figures into a specified LaTeX graphics language (for example,
PostScript(TM)). Transfig is used to create TeX documents which are portable
(i.e., they can be printed in a wide variety of environments).

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}.%{version}_%{aversion}
%patch1 -p1 -b .lib64support
%patch2 -p1 -b .includes
#%patch3 -p1 -b .strerror
#%patch4 -p1 -b .gcc4
%patch5 -p1 -b .dotsyms
%patch6 -p1 -b .tmpepsfile

%build
xmkmf
make Makefiles

%ifarch alpha
make EXTRA_DEFINES="-Dcfree=free"
%else
make CDEBUGFLAGS="$RPM_OPT_FLAGS"
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


