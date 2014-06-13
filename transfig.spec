Summary:	A utility for converting FIG files (created by xfig) to other formats
Name:		transfig
Version:	3.2.5d
Release:	11
License:	MIT
Group:		Graphics
URL:		http://www.xfig.org
Source0:	http://www.xfig.org/software/xfig/%{version}/%{name}.%{version}.tar.gz
Source100:	%name.rpmlintrc
Patch1:		transfig.3.2.5-lib64support.patch
Patch2:		transfig.3.2.5-use-tempfile-for-bitmap-eps.patch
Patch3:		transfig.3.2.5-fix-str-fmt.patch
Patch4:		transfig_optopt.patch
Patch5:		transfig.3.2.5-png1.5.patch
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	imake
BuildRequires:	tcsh

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

# Fix rpmlint error "E: non-readable"
find . -name "*.c" -o -name "*.h" -o -name README -o -name CHANGES -o -name NOTES |xargs chmod 0644

%build
xmkmf
make Makefiles

%make CDEBUGFLAGS="%{optflags}" SHLIBGLOBALSFLAGS="%{ldflags}" EXTRA_LDOPTIONS="%{ldflags}"

%install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install.man

%files
%doc CHANGES NOTES README
%{_bindir}/*
%{_mandir}/man?/*
%{_prefix}/lib/X11/xfig/bitmaps
%{_datadir}/fig2dev/*.ps

%changelog
* Tue Oct 18 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.2.5d-4mdv2012.0
+ Revision: 705070
- Update to use png1.5 api.

  + Oden Eriksson <oeriksson@mandriva.com>
    - attempt to relink against libpng15.so.15

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.5d-2
+ Revision: 670727
- mass rebuild

* Sat Jan 01 2011 Funda Wang <fwang@mandriva.org> 3.2.5d-1mdv2011.0
+ Revision: 626934
- new version 3.2.5d

* Fri Dec 31 2010 Funda Wang <fwang@mandriva.org> 3.2.5c-5mdv2011.0
+ Revision: 626810
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.5c-3mdv2011.0
+ Revision: 608040
- rebuild

* Fri Mar 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 3.2.5c-2mdv2010.1
+ Revision: 518367
- update build deps

* Wed Feb 03 2010 Lev Givon <lev@mandriva.org> 3.2.5c-1mdv2010.1
+ Revision: 500106
- Update to 3.2.5c.

* Mon Sep 28 2009 Olivier Blin <blino@mandriva.org> 3.2.5a-2mdv2010.0
+ Revision: 450399
- fix mips build failure because of optopt mismatch
  (from Arnaud Patard)

* Fri Sep 04 2009 Lev Givon <lev@mandriva.org> 3.2.5a-1mdv2010.0
+ Revision: 431413
- Update to 3.2.5a.
- Update to 3.2.5a.

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.5-4mdv2010.0
+ Revision: 427431
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 3.2.5-3mdv2009.1
+ Revision: 366387
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.2.5-2mdv2009.0
+ Revision: 225870
- rebuild

* Wed Jan 30 2008 Lev Givon <lev@mandriva.org> 3.2.5-1mdv2008.1
+ Revision: 160291
- Update to 3.2.5 final.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Fri May 25 2007 Christiaan Welvaart <spturtle@mandriva.org> 3.2.5-0.5mdv2008.0
+ Revision: 31165
- when generating bitmaps, use a tempfile for the eps to work around a crash of gs on ppc


* Mon Feb 19 2007 Emmanuel Andry <eandry@mandriva.org> 3.2.5-0.4mdv2007.0
+ Revision: 122633
- buildrequires imake
- New alpha 7
- drop patches 3 and 4, applied upstream

  + Gwenole Beauchesne <gbeauchesne@mandriva.com>
    - Fix build with newer X.org configury
    - Bunzip2 patches
    - Import transfig

* Wed Oct 05 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.2.5-0.3mdk
- merge from old ppc64-branch:
  * fix fig2dev files location
  * rename text() to do_text() to fix build on dot syms platforms

* Sat Aug 20 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.2.5-0.2mdk
- gcc4 fixes

* Mon Mar 28 2005 Daouda LO <daouda@mandrakesoft.com> 3.2.5-0.1mdk
- release for xfig-3.2.5

* Thu Dec 09 2004 Götz Waschk <waschk@linux-mandrake.com> 3.2.4-4mdk
- add html docs
- add new files
- fix buildrequires

