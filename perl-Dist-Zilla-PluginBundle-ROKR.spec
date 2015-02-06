%define upstream_name    Dist-Zilla-PluginBundle-ROKR
%define upstream_version 0.0019

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Copy README after building (for SCM inclusion, etc.)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Dist::Zilla::Plugin::CopyReadmeFromBuild)
BuildRequires:	perl(Config::Identity)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::PkgVersion)
BuildRequires:	perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Basic)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Most)
BuildArch:	noarch

%description
'@ROKR::Basic' - the Dist::Zilla::PluginBundle::ROKR::Basic manpage

This is an enhancement on the @Basic bundle (the
Dist::Zilla::PluginBundle::Basic manpage), specifically:

    @Basic (without Readme)
    CopyReadmeFromBuild
    DynamicManifest
    SurgicalPkgVersion
    SurgicalPodWeaver

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


