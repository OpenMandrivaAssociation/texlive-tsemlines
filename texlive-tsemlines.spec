# revision 23440
# category Package
# catalog-ctan /macros/latex/contrib/tsemlines/tsemlines.sty
# catalog-date 2011-06-28 13:55:08 +0200
# catalog-license pd
# catalog-version 1.0
Name:		texlive-tsemlines
Version:	1.0
Release:	11
Summary:	Support for the ancient \emline macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tsemlines/tsemlines.sty
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tsemlines.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Occasional Documents appear, that use graphics generated by
texcad from the emtex distribution. These documents often use
the \emline macro, which produced lines at an arbitrary
orientation. The present package emulates the macro, using
TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tsemlines/tsemlines.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 757139
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719810
- texlive-tsemlines
- texlive-tsemlines
- texlive-tsemlines

