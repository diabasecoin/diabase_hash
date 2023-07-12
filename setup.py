from setuptools import setup, Extension

diabase_hash_module = Extension('diabase_hash',
                                 sources = ['diabasemodule.c',
                                            'diabase.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'diabase_hash',
       version = '1.4.0',
       description = 'Binding for Diabase X11 proof of work hashing.',
       ext_modules = [diabase_hash_module])
