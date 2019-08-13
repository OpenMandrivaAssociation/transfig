Summary: A utility for converting FIG files (created by xfig) to other formats
Name: transfig
Version: 3.2.7a
Release: 1
License: MIT
Group: Graphics/Utilities
URL: https://sourceforge.net/projects/mcj/
Source0: http://downloads.sourceforge.net/mcj/fig2dev-%{version}.tar.xz
# See https://bugs.mageia.org/show_bug.cgi?id=23537
# Backported from https://sourceforge.net/p/mcj/fig2dev/ci/e0c4b02429116b15ad1568c2c425f06b95b95830/
Patch1: CVE-2018-16140.patch
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(libpng)
BuildRequires: imake
BuildRequires: tcsh
BuildRequires: ghostscript

%description
The transfig utility creates a makefile which translates FIG (created by xfig)
or PIC figures into a specified LaTeX graphics language (for example,
PostScript(TM)). Transfig is used to create TeX documents which are portable
(i.e., they can be printed in a wide variety of environments).

%prep
%setup -q -n fig2dev-%{version}
%autopatch -p1

%build
%configure --enable-transfig
%make_build

%install
%make_install

%files
%doc CHANGES NOTES README
%{_bindir}/*
%{_datadir}/fig2dev/*
%{_mandir}/man?/*
